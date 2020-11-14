import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/categories',
    name: 'Categories',
    component: () => import(/* webpackChunkName: "categories" */ '../views/Categories.vue')
  },
  {
    path: '/my-efforts',
    name: 'MyEfforts',
    component: () => import(/* webpackChunkName: "my-efforts" */ '../views/MyEfforts.vue')
  },
  {
    path: '/ranking',
    name: 'Ranking',
    component: () => import(/* webpackChunkName: "ranking" */ '../views/Ranking.vue')
  },
  {
    path: '/account',
    name: 'Account',
    component: () => import(/* webpackChunkName: "account" */ '../views/Account.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
