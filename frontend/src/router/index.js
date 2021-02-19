import Vue from 'vue'
import VueRouter from 'vue-router'
import Posts from '../views/Posts.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Posts',
    component: Posts
  },
]

const router = new VueRouter({
  routes,
  mode: "history",
  base: process.env.BASE_URL,
})

export default router
