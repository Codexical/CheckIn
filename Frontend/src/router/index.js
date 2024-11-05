import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Attendance from '../views/Attendance.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/attendance',
    name: 'Attendance',
    component: Attendance,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
