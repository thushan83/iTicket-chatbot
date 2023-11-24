//import { createApp } from 'vue'
import store from './store'
import App from './App.vue'
import Vue from 'vue'
//import router from './router'

//createApp(App).use(store).mount('#app')

import vueCustomElement from 'vue-custom-element'
import 'document-register-element/build/document-register-element'

Vue.use(vueCustomElement)
App.store = store
//App.router = router
Vue.customElement('clippy', App)
