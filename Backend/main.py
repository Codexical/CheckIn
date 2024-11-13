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


@app.post("/course/create", tags=["course"])
def create_course(course: Course):
    """
    TODO
    input: course_info
    output: course_id
    """
    course_info = course.model_dump()
    course_id = db.create_course(course_info)
    return {"course_id": course_id}


@app.post("/course/edit", tags=["course"])
def edit_course(course: Course):
    """
    TODO
    input: course_id, course_info
    output: success/fail
    """
    course_info = course.model_dump()
    success = db.edit_course(course_info)
    return {"success": success}


@app.post("/course/delete", tags=["course"])
def delete_course(course: Course):
    """
    TODO
    input: course_id
    output: success/fail
    """
    id = course.model_dump()["id"]
    success = db.delete_course(id)
    return {"success": success}


@app.get("/course/list", tags=["course"])
def list_course():
    """
    TODO
    output: course_list
    """
    course_list = db.list_courses()
    return {"course_list": course_list}


@app.post("/course/students", tags=["course"])
def list_students(course: Course):
    """
    TODO
    input: course_id
    output: student_list
    """
    id = course.model_dump()["id"]
    student_list = db.list_students(id)
    return {"student_list": student_list}


@app.post("/student/create", tags=["student"])
def create_student():
    """
    TODO
    input: student_info
    output: student_id
    """


@app.post("/student/edit", tags=["student"])
def edit_student():
    """
    TODO
    input: student_id, student_info
    output: success/fail
    """


@app.post("/student/delete", tags=["student"])
def delete_student():
    """
    TODO
    input: student_id
    output: success/fail
    """


@app.post("/student/assign-course", tags=["student"])
def assign_course():
    """
    TODO
    input: student_id, course_id
    output: success/fail
    """


@app.post("/student/roll-call", tags=["student"])
def roll_call():
    """
    TODO
    input: student_id, course_id
    output: success/fail
    """


@app.post("/student/roll-call-history", tags=["student"])
def roll_call_history():
    """
    TODO
    input: student_id, course_id
    output: roll_call_history
    """


@app.post("/teacher/create", tags=["teacher"])
def create_teacher():
    """
    TODO
    input: teacher_info
    output: teacher_id
    """


@app.post("/teacher/edit", tags=["teacher"])
def edit_teacher():
    """
    TODO
    input: teacher_id, teacher_info
    output: success/fail
    """


@app.post("/teacher/delete", tags=["teacher"])
def delete_teacher():
    """
    TODO
    input: teacher_id
    output: success/fail
    """
