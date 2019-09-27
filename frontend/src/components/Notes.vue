<template>
  <div>
    <h1>Notes</h1>
    <note-add-element />
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

export default {
    name: "Notes",
    components: {
        Note,
        NoteAddElement,
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
                this.notes = data.notes
            }
        }
    }
}
</script>

<style scoped>
h1 {
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
