<template>
  <div>
    <div id="note-add-div">
      <div class="element-div">
        <label for="title-input">Title:</label>
        <label for="description-input">Description:</label>
      </div>
      <div class="element-div">
        <input
          id="title-input"
          v-model="title"
          maxlength="50"
        >
        <input
          id="description-input"
          v-model="description"
          maxlength="200"
        >
      </div>
      <select
        id="color"
        v-model="color"
        md-dense
      >
        <option
          v-for="c in colors"
          :key="c"
        >
          {{ c }}
        </option>
      </select>
      <md-button
        class="md-primary md-raised"
        @click="addNote"
      >
        Add
      </md-button>
    </div>
  </div>
</template>
<script>
export default {
    name: "NoteAddElement",
    data: function() {
        return {
            title: "",
            description: "",
            color: this.getRandomColor(),
            colors: this.getColors(),
        }
    },
    methods: {
        getColors() {
            return [
                "blue",
                "white",
                "red",
                "green",
                "black"
            ]
        },
        getRandomColor() {
            const colors = this.getColors();
            return colors[Math.floor(Math.random()*colors.length)]
        },
        addNote() {
            this.$socket.sendObj(
              {"note": {
                title: this.title, 
                description: this.description, 
                color: this.color}
              });
            this.title = "";
            this.description = "";
            this.color = this.getRandomColor();
        }
    }
}
</script>
<style scoped>
div {
    display: flex;
    justify-content: space-between;
}
.element-div {
    flex-direction: column;
}
#note-add-div {
    flex-direction: row;
}
input {
    margin-top: 1%;
    margin-right: 5px;
    margin-left: 5px;
}
label {
    margin-right: 20%;
    margin-top: 2%;
}
</style>
