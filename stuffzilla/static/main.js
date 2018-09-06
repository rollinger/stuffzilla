import Vue from 'vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'
import VueAnalytics from 'vue-analytics'

import VueRaven from 'vue-raven'


import Sharezilla from './Sharezilla.vue'

// Axios csrf settings
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


// Sentry for logging frontend errors
if (process.env.NODE_ENV === 'production') {Vue.use(VueRaven, {dsn: SENTRY_PUBLIC_DSN})}



// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {id: GOOGLE_ANALYTICS, router})



Vue.use(Meta)


/* eslint-disable no-new */
// Root Instance
new Vue({
    el: '#sharezilla-main',
    router,
    store,
    render: h => h(Sharezilla),
})
