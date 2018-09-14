import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'
import VueAnalytics from 'vue-analytics'

import VueRaven from 'vue-raven'

// Import Styles & Foundation
//https://stevenwestmoreland.com/2018/01/how-to-include-bootstrap-in-your-project-with-webpack.html

import 'popper.js';
// Bootstrap.js and Bootstrap-Vue alongside?
import 'bootstrap';
import './scss/app.scss';
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Sharezilla from './Sharezilla.vue'

// Axios csrf settings
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


// Sentry for logging frontend errors
if (process.env.NODE_ENV === 'production') {Vue.use(VueRaven, {dsn: SENTRY_PUBLIC_DSN})}



// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {id: GOOGLE_ANALYTICS, router})

//https://bootstrap-vue.js.org/
Vue.use(BootstrapVue)


Vue.use(Meta)


/* eslint-disable no-new */
// Root Instance
new Vue({
    el: '#sharezilla-main',
    router,
    store,
    render: h => h(Sharezilla),
})
