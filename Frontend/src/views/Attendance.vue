<template>
  <div>
    <h1>點名畫面</h1>

    <!-- 現在時間 -->
    <p>現在時間：{{ currentTime }}</p>

    <!-- 課程選擇 -->
    <label for="course-select">課程列表：</label>
    <select id="course-select" v-model="selectedCourse" @change="fetchStudents">
      <option v-for="course in courses" :key="course.id" :value="course.name">
        {{ course.name }}
      </option>
    </select>

    <!-- 學生列表 -->
    <div v-if="students.length > 0">
      <ul>
        <li v-for="student in students" :key="student.id">
          <span>{{ student.name }}</span>
          <button @click="toggleAttendance(student.id)">
            {{ attendance[student.id] ? "取消出席" : "出席" }}
          </button>
          <button @click="goToDetails(student.id)" style="margin-left: 10px;">
            詳細資料
          </button>
          <span style="margin-left: 10px;">
            狀態：{{ attendance[student.id] ? "已出席" : "未出席" }}
          </span>
        </li>
      </ul>
    </div>
    <p v-else>請選擇課程以顯示學生名單。</p>

    <!-- 提交按鈕 -->
    <button class = "submit-btn" @click="submitAttendance">
      提交出席狀態
    </button>

    <!-- 新增學生按鈕-->
    <button @click = "goToCreateStudent" class = "create-student-btn">
      新增學生
    </button>
  </div>
</template>

<script>
export default {
  name: "AttendancePage",
  data() {
    return {
      currentTime: new Date().toLocaleString(), // 顯示當前時間
      courses: [], // 存放課程列表
      selectedCourse: null, // 選中的課程
      students: [], // 存放學生名單
      attendance: {}, // 存放每個學生的出席狀態
    };
  },
  methods: {
    // 模擬從後端獲取課程列表
    fetchCourses() {
      this.courses = [
        { id: 1, name: "A" },
        { id: 2, name: "B" },
      ];
    },

    // 根據選課篩選學生列表
    fetchStudents() {
      const allStudents = [
        {
          id: 101,
          name: "學生A",
          school: "A中學",
          gender: "男",
          phone: "123456789",
          courses: ["A"],
        },
        {
          id: 102,
          name: "學生B",
          school: "B中學",
          gender: "女",
          phone: "987654321",
          courses: ["B"],
        },
        {
          id: 103,
          name: "學生C",
          school: "C中學",
          gender: "男",
          phone: "555555555",
          courses: ["A", "B"],
        },
      ];

      // 篩選出修該課程的學生
      if (this.selectedCourse) {
        this.students = allStudents.filter((student) =>
          student.courses.includes(this.selectedCourse)
        );
      } else {
        this.students = []; // 未選擇課程時清空學生名單
      }

      // 初始化每個學生的出席狀態
      this.attendance = this.students.reduce((acc, student) => {
        acc[student.id] = false; // 默認未出席
        return acc;
      }, {});
    },

    // 切換學生的出席狀態
    toggleAttendance(studentId) {
      this.attendance[studentId] = !this.attendance[studentId];
    },

    // 跳轉到學生詳細資料頁
    goToDetails(studentId) {
      this.$router.push({ name: "StudentDetail", params: { id: studentId } });
    },

    // 提交出席狀態到後端
    submitAttendance() {
      const attendanceData = {
        courseId: this.selectedCourse,
        attendance: this.attendance, // 包含每個學生的出席狀態
      };

      console.log("提交出席數據：", attendanceData);
    },

    goToCreateStudent(){
      this.$router.push({ name: 'CreateStudent'});
    },

    updateTime() {
      this.currentTime = new Date().toLocaleString();
    },
  },
  mounted() {
    this.fetchCourses();
    this.timer = setInterval(this.updateTime, 1000);
  },
  beforeUnmount() {
    clearInterval(this.timer);
  },
};
</script>

<style scoped>
label {
  font-weight: bold;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  justify-content: center;
  margin: 10px 0;
  display: flex;
  align-items: center;
}
button {
  margin-left: 10px;
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
.submit-btn {
  margin-left: 10px;
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.submit-btn:hover {
  background-color: #0056b3;
}
.create-student-btn {
  display: block;
  margin: 10px auto;
  padding: 5px 10px;
  background-color: #4caf50;
  color: while;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.create-student-btn:hover{
  background-color: #45a049;
}
</style>
