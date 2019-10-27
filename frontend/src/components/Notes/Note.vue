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
        <md-button @click="expire">
          <md-icon>access_time</md-icon> {{ expireText }}
        </md-button>
        <md-button @click="deleteNote">
          Delete
        </md-button>
      </md-card-actions>
    </md-card>
  </div>
</template>
<script>
import { EXPIRES, EXPIRES_IN_SECONDS } from "./config";

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
    data() {
      return {
        expireNumber: 0,
      }
    },
    computed: {
      expireText: function() {
        if (this.expireNumber == EXPIRES.THIRTY_MINUTES) {
          return "30 minutes";
        }
        if (this.expireNumber == EXPIRES.ONE_HOUR) {
          return "1 hour";
        }
        if (this.expireNumber == EXPIRES.FIVE_HOURS) {
          return "5 hours";
        }
        if (this.expireNumber == EXPIRES.FIFTEEN_HOURS) {
          return "15 hours";
        }
        if (this.expireNumber == EXPIRES.ONE_DAY) {
          return "1 day";
        }
        if (this.expireNumber == EXPIRES.ONE_WEEK) {
          return "1 week";
        }
        return "Never";
      }
    },
    methods: {
      deleteNote() {
        this.$socket.sendObj({note_delete: this.id});
      },
      expire() {
        this.expireNumber += 1;
        if (this.expireNumber > Object.keys(EXPIRES).length) {
          this.expireNumber = 0;
        }
        this.$socket.sendObj({
          note_expire: {
            "id": this.id, 
            "expire": EXPIRES_IN_SECONDS[this.expireNumber]
          }
        });
      }
    }
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
