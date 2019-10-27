<template>
  <div id="notes">
    <user-count id="user-count" />
    <note-add-element id="note-add-element" />
    <div id="note-container">
      <Note
        v-for="note in notes"
        :id="note.id"
        :key="`${note.id} ${componentKey}`"
        :title="note.title"
        :color="note.color"
        :description="note.description"
        :expire-at="note.expire_at"
      />
    </div>
  </div>
</template>
<script>
import Note from "./Notes/Note.vue";
import NoteAddElement from "./Notes/NoteAddElement.vue";
import UserCount from "./UserCount.vue";

export default {
    name: "Notes",
    components: {
        Note,
        NoteAddElement,
        UserCount,
    },
    data() {
        return {
            componentKey: 0,
            "notes": [{
                "title": "",
                "description": "",
                "color": "white",
                "id": 0,
                "expireAt": ""
            }]
        }
    },
    beforeMount() {
        this.$options.sockets.onmessage = (msg) => {
            const data = JSON.parse(msg.data);
            if (data.notes) {
                this.notes = data.notes;
            }
        }
    },
    mounted() {
      window.setInterval(() => {
        if (this.$socket.readyState === this.$socket.OPEN) {
          this.$socket.sendObj({"update_request": true});
          // this will force an update of all notes.
          // Find a better way to do this maybe
          this.componentKey += 1;
        }
      }, 1000 * 60);
      if(this.$socket.readyState === this.$socket.OPEN) {
          this.$socket.sendObj({"update_request": true});
      }
    }
}
</script>

<style scoped>
#user-count {
    text-align: center;
}
#note-add-element {
    justify-content: center;
}
#notes {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
  overflow: hidden;
}
#note-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: flex-start;
  align-items: baseline;
  align-content: center;
  width: 100%;
}
</style>
