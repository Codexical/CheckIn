import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Attendance from '../views/Attendance.vue';
import StudentDetail from '../views/StudentDetail.vue';
import CreateStudent from '../views/CreateStudent.vue'; // 引入新增學生頁面

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
    props: true,
  },
  {
    path: '/student/create', // 新增的路由
    name: 'CreateStudent',
    component: CreateStudent, // 指向新增學生頁面
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
