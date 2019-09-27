<template>
  <div>
    <p id="user-count">
      Users online: {{ usersOnline }}
    </p>
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
    p {
        font-size: 30px;
    }
</style>
