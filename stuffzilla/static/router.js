import Vue from 'vue'
import VueRouter from 'vue-router'

import MarketComponent from './components/structural/MarketComponent.vue'
import ProfileComponent from './components/structural/ProfileComponent.vue'

const routes = [
    {path: '*', component: MarketComponent},
    {path: '/profile', component: ProfileComponent},
]

Vue.use(VueRouter)

const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes
})

export default router
