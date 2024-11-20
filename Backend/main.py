from fastapi import FastAPI
from pydantic import BaseModel
from db import Database

app = FastAPI()

db = Database("CheckIn.db")


class Student(BaseModel):
    id: int
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
def edit_course(course: Course):
    """
    TODO
    input: course_id, course_info
    output: success/fail
    """
    course_info = course.model_dump()
    success = db.edit_course(course_info)
    return {"success": success}


@app.delete("/course/{courseID}", tags=["course"], summary="Delete course")
def delete_course(course: Course):
    """
    TODO
    input: course_id
    output: success/fail
    """
    id = course.model_dump()["id"]
    success = db.delete_course(id)
    return {"success": success}


@app.get("/course/list", tags=["course"], summary="List courses")
def list_course():
    """
    TODO
    output: course_list
    """
    course_list = db.list_courses()
    return {"course_list": course_list}


@app.get("/course/{courseID}/students", tags=["course"], summary="List course students")
def list_students(course: Course):
    """
    TODO
    input: course_id
    output: student_list
    """
    id = course.model_dump()["id"]
    student_list = db.list_students(id)
    return {"student_list": student_list}


@app.post("/student", tags=["student"], summary="Create student")
def create_student():
    """
    TODO
    input: student_info
    output: student_id
    """


@app.patch("/student/{studentID}", tags=["student"], summary="Edit student")
def edit_student():
    """
    TODO
    input: student_id, student_info
    output: success/fail
    """


@app.delete("/student/{studentID}", tags=["student"], summary="Delete student")
def delete_student():
    """
    TODO
    input: student_id
    output: success/fail
    """


@app.patch("/student/{studentID}/course", tags=["student"], summary="Assign course")
def assign_course():
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


@app.get("/student/{studentID}/roll-call-history", tags=["student"], summary="Roll call history")
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
