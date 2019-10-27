from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Note
from django.core.serializers.json import DjangoJSONEncoder
import json
import redis
import os
import maya


redis_ip = os.getenv("REDIS_IP", "127.0.0.1")
r = redis.Redis(host=redis_ip)
r.set("number", 0)
r.set("users_online", 0)


class WeeappsWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "weeapps"
        self.room_group_name = "weeapps"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        r.incr("users_online")
        self.update_client()

    def update_client(self):
        self.send_status()
        self.send_notes()

    def send_notes(self):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "send_notes_event"}
        )

    def send_notes_event(self, event):
        fields = ["id", "title", "description", "color", "expire_at"]
        notes = Note.objects.all().values(*fields)
        self.send(text_data=json.dumps({"notes": list(notes)}, cls=DjangoJSONEncoder))

    def send_status(self):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "user_update_event"}
        )

    def user_update_event(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "number": int(r.get("number")),
                    "usersOnline": int(r.get("users_online")),
                }
            )
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        r.decr("users_online")
        self.send_status()

    def receive_number(self, text_data_json):
        operation = text_data_json["operation"]
        if operation == "+":
            r.incr("number")
        elif operation == "-":
            r.decr("number")
        elif operation == "reset":
            r.set("number", 0)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "counter_event"}
        )

    def receive_notes(self, text_data_json):
        note = text_data_json["note"]
        Note.objects.create(**note)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "send_notes_event"}
        )

    def receive_notes_delete(self, text_data_json):
        note_delete = text_data_json["note_delete"]
        Note.objects.get(id=note_delete).delete()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "send_notes_event"}
        )

    def receive_notes_expire(self, text_data_json):
        note_expire = text_data_json["note_expire"]
        note = Note.objects.get(id=note_expire["id"])
        expire = note_expire["expire"]
        if expire == -1:
            note.expire_at = None
        else:
            if note.expire_at:
                temp_expire_at = maya.MayaDT.from_datetime(note.expire_at)
            else:
                temp_expire_at = maya.now()
            temp_expire_at = temp_expire_at.add(seconds=expire)
            note.expire_at = temp_expire_at.datetime()
        note.save()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "send_notes_event"}
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json.get("operation"):
            self.receive_number(text_data_json)
        elif text_data_json.get("note"):
            self.receive_notes(text_data_json)
        elif text_data_json.get("note_delete"):
            self.receive_notes_delete(text_data_json)
        elif text_data_json.get("note_expire"):
            self.receive_notes_expire(text_data_json)
        elif text_data_json.get("update_request"):
            self.update_client()

    def counter_event(self, event):
        self.send(text_data=json.dumps({"number": int(r.get("number"))}))
