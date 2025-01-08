<script>
import { fetchCourses } from "../api/course";

export default {
  data() {
    return {
      courses: []
    };
  },
  async mounted() {
    try {
      const response = await fetchCourses();
      this.courses = response.data.course_list;
    } catch (error) {
      console.error("Failed to fetch courses:", error);
    }
  }
};
</script>
