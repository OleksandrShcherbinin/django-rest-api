import Vue from 'vue'
import VueRouter from 'vue-router'
import Posts from '../views/Posts.vue'
import Signup from "@/views/Signup";
import Logout from "@/views/Logout";
import Login from "@/views/Login";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Posts',
    component: Posts
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
      {
    path: '/login',
    name: 'Login',
    component: Login
  },
      {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
]

const router = new VueRouter({
  routes,
  mode: "history",
  base: process.env.BASE_URL,
})

export default router
