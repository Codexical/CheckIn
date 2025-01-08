import apiClient from "./api";

export function fetchCourses() {
  return apiClient.get("/course/list");
}
