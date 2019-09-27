import Vue from "vue";
import App from "./App.vue";
import { MdButton, MdCard } from "vue-material/dist/components";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";
import VueRouter from "vue-router";
import Counter from "./components/Counter.vue";
import Notes from "./components/Notes.vue";
import Main from "./components/Main.vue";
import VueNativeSock from "vue-native-websocket";

Vue.use(MdCard);
Vue.use(MdButton);
Vue.use(VueRouter);

Vue.config.productionTip = false;

const router = new VueRouter({
  base: __dirname,
  routes: [
    { path: "/", component: Main },
    { path: "/counter", component: Counter },
    { path: "/notes", component: Notes }
  ]
});

const websocketServer =
  process.env.VUE_APP_WEBSOCKET_SERVER_URL || "ws://127.0.0.1:8000";
Vue.use(VueNativeSock, `${websocketServer}/ws/`, { format: "json" });

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
