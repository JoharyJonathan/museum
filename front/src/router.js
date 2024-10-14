import { createRouter, createWebHistory } from 'vue-router';
import Home from './views/Home.vue';
import About from './views/About.vue';
import SignUp from './views/SignUp.vue';
import Login from './views/Login.vue';
import Profile from './views/Profile.vue';

const routes = [
  {
    path: '/',
    name: 'home-page',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile,
    meta: { requiresAuth: true }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Verify authentification
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token');
  if (to.matched.some(record => record.meta.requiresAuth) && !token) {
    next('/login');
  } else {
    next();
  }
});

export default router;
