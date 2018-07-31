import Vue from 'vue'
import VueRouter from 'vue-router'

import TitleComponent from './components/TitleComponent.vue'
import SearchComponent from './components/SearchComponent.vue'
import ShareComponent from './components/ShareComponent.vue'

const routes = [
    {path: '*', component: TitleComponent},
    {path: '/search', component: SearchComponent},
    {path: '/share', component: ShareComponent}
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes
})

export default router
