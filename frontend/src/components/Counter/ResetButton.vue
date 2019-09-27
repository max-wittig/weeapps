<template>
  <div>
    <MdButton
      class="md-raised"
      @click="resetNumber"
    >
      Reset
    </MdButton>
  </div>
</template>

<script>
export default {
    name: "ResetButton",
    methods: {
        resetNumber() {
            this.$socket.sendObj({operation: "reset"});
        },
    }
}
</script>
<style scoped>
    div { outline-style:none;}
    ::-moz-selection { background:transparent; }
    ::selection { background:transparent; }
</style>
