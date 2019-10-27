<template>
  <div>
    <h1
      :class="color" 
      @click="clickAddNumber"
      @contextmenu="clickSubtractNumber($event)"
    >
      {{ number }}
    </h1>
  </div>
</template>

<script>
export default {
    name: "NumberDisplay",
    data() {
        return {
            "number": "0",
        }
    },
    computed: {
        color() {
            if (this.number == 0) {
                return "neutral-number"
            }
            return this.number > 0 ? "positive-number" : "negative-number"
        }
    },
    beforeMount() {
        this.$options.sockets.onmessage = (msg) => {
            const data = JSON.parse(msg.data);
            if (data.number || data.number === 0) {
                this.number = data.number;
            }
        }
    },
    methods: {
        clickAddNumber() {
            // $socket is [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) instance
            this.$socket.sendObj({operation: "+"});
        },
        clickSubtractNumber(e) {
          this.$socket.sendObj({operation: "-"});
          e.preventDefault();
        }
    }
}
</script>
<style scoped>
    .positive-number {
        color: darkgreen;
    }
    .negative-number {
        color: darkred;
    }
    .neutral-number {
        color: black;
    }
    h1 {
        font-size: 300px;
        cursor: pointer;
        user-select: none;
    }
    div { outline-style:none;}
    ::-moz-selection { background:transparent; }
    ::selection { background:transparent; }
</style>
