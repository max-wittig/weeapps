<template>
  <div>
    <span class="md-title">
      Users online: {{ usersOnline }}
    </span>
  </div>
</template>

<script>
export default {
    name: "UserCount",
    data() {
        return {"usersOnline": "0"}
    },
    beforeMount() {
        this.$options.sockets.onmessage = (msg) => {
            let usersOnline = JSON.parse(msg.data).usersOnline;
            if (usersOnline) {
                this.usersOnline = usersOnline
            }
        }
    }
}
</script>
<style scoped>
</style>
