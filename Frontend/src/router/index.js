import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Attendance from '../views/Attendance.vue';
import StudentDetail from '../views/StudentDetail.vue';

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
  {
    path: '/studentdetail/:id',
    name: 'StudentDetail',
    component: StudentDetail,
    props:true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
