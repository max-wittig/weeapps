<template>
  <div>
    <h1>Home</h1>
    <router-link to="/notes">
      <h2>Notes</h2>
      <img
        width="100px"
        height="100px" 
        src="images/notes.png"
      >
    </router-link>
    <router-link to="/counter">
      <h2>Counter</h2>
      <img
        width="100px"
        height="100px" 
        src="images/counter.png"
      >
    </router-link>
  </div>
</template>
<script>
export default {
    name: "Main"
}
</script>
<style scoped>
h1 {
    text-decoration: underline;
}
img {
    border: 1px solid black;
}
div {
    align-self: flex-end;
    text-align: center;
}
</style>
