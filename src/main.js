import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import './axios'
import store from './vuex'
import VueCookies from 'vue-cookies';

Vue.config.productionTip = false
Vue.use(VueCookies);
Vue.$cookies.config({httpOnly: true})
new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
