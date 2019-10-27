<template>
  <div id="app">
    <div class="page-container">
      <md-app>
        <md-app-toolbar class="md-primary">
          <span class="md-title">
            WeeApps
          </span>
          <div class="md-toolbar-section-end">
            <user-count id="user-count" />
          </div>
        </md-app-toolbar>
        <md-app-content id="content">
          <router-view />
        </md-app-content>
      </md-app>
    </div>
  </div>
</template>

<script>
import UserCount from "./components/UserCount";

export default {
  name: "App",
  components: {
    UserCount
  },
  data: () => ({
    menuVisible: false
  })
};
</script>
<style>
#content {
  background-color: aliceblue;
}
body {
  background-color: aliceblue;
}
</style>
