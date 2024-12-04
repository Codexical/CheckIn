<template>
    <div>
      <!-- 如果學生資料存在，顯示詳細信息 -->
      <h1 v-if="student">學生詳細資料</h1>
      <div v-else>
        <p>正在加載學生資料...</p>
      </div>
      <p v-if="student">學生 ID：{{ id }}</p>
      <p v-if="student">學生姓名：{{ student.name }}</p>
      <p v-if="student">學校：{{ student.school }}</p>
      <p v-if="student">性別：{{ student.gender }}</p>
      <p v-if="student">電話：{{ student.phone }}</p>
  
      <!-- 顯示修過的課程 -->
      <p v-if="student">修過的課程：</p>
      <ul v-if="student && student.courses.length > 0">
        <li v-for="(course, index) in student.courses" :key="index">
          {{ course }}
        </li>
      </ul>
      <p v-else>未修過任何課程</p>
  
      <button @click="goBack">返回</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'StudentDetailPage',
    props: ['id'], // 接收路由參數
    data() {
      return {
        student: null, // 學生詳細資料
      };
    },
    created() {
      // 模擬根據 ID 獲取學生詳細資料
      const students = [
        {
          id: 101,
          name: '學生A',
          school: 'A中學',
          gender: '男',
          phone: '123456789',
          classes: 3,
          courses: ['A'], // 修過的課程
        },
        {
          id: 102,
          name: '學生B',
          school: 'B中學',
          gender: '女',
          phone: '987654321',
          classes: 4,
          courses: ['B'], // 修過的課程
        },
        {
          id: 103,
          name: '學生C',
          school: 'C中學',
          gender: '男',
          phone: '555555555',
          classes: 2,
          courses: ['A', 'B'], // 修過的課程
        },
      ];
      // 根據 ID 查找對應的學生
      this.student = students.find((s) => s.id === parseInt(this.id));
    },
    methods: {
      goBack() {
        this.$router.push('/attendance');
      },
    },
  };
  </script>
  
  <style scoped>
  button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }
  </style>
  