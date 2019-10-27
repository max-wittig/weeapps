import Vue from "vue";
import App from "./App.vue";
import {
  MdButton,
  MdCard,
  MdIcon,
  MdApp,
  MdTabs,
  MdContent,
  MdDrawer,
  MdMenu,
} from "vue-material/dist/components";
import MdAppToolBar from "vue-material/dist/components/MdApp";
import MdListItem from "vue-material/dist/components/MdList";
import MdToolBar from "vue-material/dist/components/MdToolbar";
import MdSelect from "vue-material/dist/components/MdField";
import MdOption from "vue-material/dist/components/MdField";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";
import VueRouter from "vue-router";
import Counter from "./components/Counter.vue";
import Notes from "./components/Notes.vue";
import Main from "./components/Main.vue";
import VueNativeSock from "vue-native-websocket";

Vue.use(MdIcon);
Vue.use(MdCard);
Vue.use(MdButton);
Vue.use(MdApp);
Vue.use(MdTabs);
Vue.use(MdAppToolBar);
Vue.use(MdContent);
Vue.use(MdListItem);
Vue.use(MdDrawer);
Vue.use(MdToolBar);
Vue.use(MdSelect);
Vue.use(MdOption);
Vue.use(MdMenu);
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

import moment from "moment";
Object.defineProperty(Vue.prototype, "$moment", { value: moment });

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
