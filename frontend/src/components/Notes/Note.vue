<template>
  <div>
    <md-card :class="color">
      <md-card-header>
        <div class="md-title">
          {{ title }}
        </div>
      </md-card-header>

      <md-card-content>
        {{ description }}
      </md-card-content>

      <md-card-actions>
        <md-button @click="deleteNote">
          Delete
        </md-button>
      </md-card-actions>
    </md-card>
  </div>
</template>
<script>
export default {
    name: "Note",
    props: {
        title: {
          type: String,
          default: "",
          required: true,
        },
        description: {
          type: String,
          default: "",
          required: true,
        },
        color: {
          type: String,
          default: "white",
          required: true,
        },
        id: {
          type: Number,
          default: -1,
          required: true,
        }
    },
    methods: {
      deleteNote() {
        this.$socket.sendObj({note_delete: this.id});
      }
    },
}
</script>
<style scoped>
  .md-card {
    width: 320px;
    margin: 4px;
    vertical-align: top;
    align-self: flex-end;
    order: unset;
  }
  .white {
    background-color: white;
  }
  .green {
      background-color: lightgreen;
  }
  .red {
      background-color: lightpink;
  }
  .blue {
      background-color: lightblue;
  }
  .black {
      background-color: darkgrey;
  }
</style>
