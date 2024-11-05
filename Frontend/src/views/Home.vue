<template>
  <div>
    <h1>歡迎來到點名系統</h1>
    <button @click="goToAttendance">點名</button>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    goToAttendance() {
      this.$router.push('/attendance');
    },
  },
};
</script>