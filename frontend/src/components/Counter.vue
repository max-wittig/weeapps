<template>
  <div id="counter">
    <number-display number="0" />
    <reset-button />
  </div>
</template>

<script>
import NumberDisplay from "./Counter/NumberDisplay.vue";
import ResetButton from "./Counter/ResetButton.vue";

export default {
  name: "Counter",
  components: {
    NumberDisplay,
    ResetButton,
  },
  mounted() {
    if(this.$socket.readyState === this.$socket.OPEN) {
        this.$socket.sendObj({"update_request": true});
    }
  }
};
</script>

<style scoped>
#counter {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
