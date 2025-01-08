<template>
    <div class="create-student">
      <h1>新增學生</h1>
      <form @submit.prevent="submitForm">
        <!-- 學生姓名 -->
        <label for="name">學生姓名:</label>
        <input type="text" id="name" v-model="student.name" required />
  
        <!-- 學生年齡 -->
        <label for="school">學校:</label>
        <input type="string" id="school" v-model="student.school" required />

        <!-- 學生性別 -->
        <label for="gender">性別:</label>
        <input type="string" id="gender" v-model="student.gender" required />

        <!-- 提交按鈕 -->
        <button type="submit" class="submit-btn">提交</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        student: {
          name: "",
          age: null,
        },
      };
    },
    methods: {
      submitForm() {
        console.log("新增學生數據：", this.student);
        alert("學生新增成功！");
        this.$router.push("/attendance"); // 提交成功後跳轉回點名頁面
      },
    },
  };
  </script>
  
  <style scoped>
  .create-student {
    text-align: center;
    margin-top: 20px;
  }
  form {
    display: inline-block;
    text-align: left;
  }
  label {
    display: block;
    margin: 10px 0 5px;
  }
  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
  }
  button {
    background-color: #4caf50;
    color: white;
    padding: 10px 20px;
    font-size: 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
  </style>
  