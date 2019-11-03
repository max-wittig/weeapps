<template>
  <div>
    <md-card :class="color">
      <md-card-header>
        <div v-if="expireIn">
          Expires in {{ expireIn }} minutes
        </div>
        <div v-else>
          Expires never
        </div>
        <div class="md-title">
          {{ title }}
        </div>
      </md-card-header>

      <md-card-content>
        {{ description }}
      </md-card-content>

      <md-card-actions>
        <md-button @click="expire(-1)">
          <md-icon>access_time</md-icon> Reset
        </md-button>
        <md-button @click="expire(60 * 60)">
          <md-icon>access_time</md-icon> +1 hour
        </md-button>
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
        },
        expireAt: {
          type: String,
          default: "",
          required: false,
        }
    },
    computed: {
      expireIn: function() {
        return this.$moment(this.expireAt).diff(this.$moment(), "minutes");
      },
    },
    mounted() {
      // this seems hacky. Every note is created from scratch
      // every minute
      if (this.expireIn <= 0) {
        this.deleteNote();
      }
    },
    methods: {
      deleteNote() {
        this.$socket.sendObj({note_delete: this.id});
      },
      expire(seconds) {
        this.$socket.sendObj({
          note_expire: {
            "id": this.id, 
            "expire": seconds,
          }
        });
      }
    }
}
</script>
<style scoped>
  .md-card {
    min-width: 10vw;
    width: 20vw;
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
