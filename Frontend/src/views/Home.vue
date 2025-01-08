<template>
  <div class="home">
    <h1 class="title">歡迎來到點名系統</h1>
    <button class="btn" @click="goToAttendance">點名</button>
    <h2 class="subtitle">課程列表</h2>
    <CourseList />
  </div>
</template>

<script>
import CourseList from "../components/CourseList.vue"; // 引入課程列表組件

export default {
  name: "HomePage",
  components: {
    CourseList, // 註冊 CourseList 組件
  },
  methods: {
    goToAttendance() {
      this.$router.push("/attendance"); // 路由導航到點名頁面
    },
  },
};
</script>

<style scoped>
/* 樣式部分 */
.home {
  text-align: center;
  margin-top: 50px;
}

.title {
  font-size: 2em;
  color: #333;
}

.subtitle {
  margin-top: 20px;
  font-size: 1.5em;
  color: #555;
}

.btn {
  background-color: #4caf50;
  color: white;
  padding: 10px 20px;
  font-size: 1em;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-bottom: 20px;
}

.btn:hover {
  background-color: #45a049;
}
</style>
