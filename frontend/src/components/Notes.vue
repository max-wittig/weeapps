<template>
  <div id="notes">
    <user-count />
    <note-add-element id="note-add-element" />
    <div id="note-container">
      <Note
        v-for="note in notes" 
        :id="note.id"
        :key="note.id"
        :title="note.title"
        :color="note.color"
        :description="note.description"
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
            "notes": [{"title": "", "description": "", "color": "white", "id": 0}]
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
        if(this.$socket.readyState === this.$socket.OPEN) {
            this.$socket.sendObj({"update_request": true});
        }
    }
}
</script>

<style scoped>
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
  text-align: center;
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
