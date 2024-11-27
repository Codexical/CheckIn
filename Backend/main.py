from fastapi import FastAPI
from pydantic import BaseModel
from db import Database
from student_db import StudentDatabase

app = FastAPI()

db = Database("CheckIn.db")
student_db = StudentDatabase("Student_info.db")


class Student(BaseModel):
    name: str
    course_id: int
    birth: str
    school_name: str
    school_grade: str
    parent_name: str
    mobile: str
    phone: str


class Course(BaseModel):
    id: int
    course_name: str
    teacher_id: int
    course_time: str


class Teacher(BaseModel):
    id: int
    name: str


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/course", tags=["course"], summary="Create course")
def create_course(course: Course):
    """
    TODO
    input: course_info
    output: course_id
    """
    course_info = course.model_dump()
    course_id = db.create_course(course_info)
    return {"course_id": course_id}


@app.patch("/course/{courseID}", tags=["course"], summary="Edit course")
def edit_course(courseID: int, course: Course):
    """
    TODO
    input: course_id, course_info
    output: success/fail
    """
    course_info = course.model_dump()
    if courseID != course_info["id"]:
        return {"message": "courseID does not match course info"}
    success = db.edit_course(course_info)
    return {"message": "success" if success else "fail"}


@app.delete("/course/{courseID}", tags=["course"], summary="Delete course")
def delete_course(courseID: int, course: Course):
    """
    TODO
    input: course_id
    output: success/fail
    """
    id = course.model_dump()["id"]
    if courseID != id:
        return {"message": "courseID does not match course info"}
    success = db.delete_course(id)
    return {"success": "success" if success else "fail"}


@app.get("/course/list", tags=["course"], summary="List courses")
def list_course():
    """
    TODO
    output: course_list
    """
    course_list = db.list_courses()
    return {"course_list": course_list}


@app.get("/course/{courseID}/students", tags=["course"], summary="List course students")
def list_students(courseID: int, course: Course):
    """
    TODO
    input: course_id
    output: student_list
    """
    id = course.model_dump()["id"]
    if courseID != id:
        return {"message": "courseID does not match course info"}
    student_list = db.list_students(id)
    return {"student_list": student_list}


@app.post("/student", tags=["student"], summary="Create student")
def create_student(student: Student):
    """
    TODO
    Add a student into database
    input: student_info
    output: student_id
    """
    student_info = student.model_dump()
    id = student_db.create_student(student_info)
    return {"student_id": id}


@app.patch("/student/{studentID}", tags=["student"], summary="Edit student")
def edit_student(studentID: int, student: Student):
    """
    TODO
    Edit a student information from database
    input: student_id, student_info
    output: success/fail
    """
    student_info = student.model_dump()
    print(student_info)
    success = student_db.edit_student(student_info, studentID)
    return {"success": success}


@app.delete("/student/{studentID}", tags=["student"], summary="Delete student")
def delete_student(studentID: int):
    """
    TODO
    Delete a student from database
    input: student_id
    output: success/fail
    """
    # id = student.model_dump()["id"]
    success = student_db.delete_student(studentID)
    return {"success": success}


@app.get("/student/list", tags=["student"], summary="List student")
def get_student():
    """
    TODO
    return student_list
    """
    student_list = student_db.list_courses()
    return {"student_list": student_list}


@app.patch("/student/{studentID}/course", tags=["student"], summary="Assign course")
def assign_course(student: Student):
    """
    TODO
    input: student_id, course_id
    output: success/fail
    """


@app.post("/student/{studentID}/roll-call", tags=["student"], summary="Roll call")
def roll_call():
    """
    TODO
    input: student_id, course_id
    output: success/fail
    """


@app.get(
    "/student/{studentID}/roll-call-history",
    tags=["student"],
    summary="Roll call history",
)
def roll_call_history():
    """
    TODO
    input: student_id, course_id
    output: roll_call_history
    """


@app.post("/teacher", tags=["teacher"], summary="Create teacher")
def create_teacher():
    """
    TODO
    input: teacher_info
    output: teacher_id
    """


@app.patch("/teacher/{teacherID}", tags=["teacher"], summary="Edit teacher")
def edit_teacher():
    """
    TODO
    input: teacher_id, teacher_info
    output: success/fail
    """


@app.delete("/teacher/{teacherID}", tags=["teacher"], summary="Delete teacher")
def delete_teacher():
    """
    TODO
    input: teacher_id
    output: success/fail
    """
