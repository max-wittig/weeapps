<template>
  <div id="counter">
    <user-count users-online="0" />
    <number-display number="0" />
    <reset-button />
  </div>
</template>

<script>
import NumberDisplay from "./Counter/NumberDisplay.vue";
import ResetButton from "./Counter/ResetButton.vue";
import UserCount from "./UserCount.vue";

export default {
  name: "Counter",
  components: {
    NumberDisplay,
    UserCount,
    ResetButton,
  },
  mounted() {
    if(this.$socket.readyState === this.$socket.OPEN) {
        this.$socket.sendObj({"update_request": true});
    }
  }
};
</script>

<style>
body {
  height: 100%;
  overflow-y: hidden;
}
#counter {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
  overflow: hidden;
  text-align: center;
}
</style>
