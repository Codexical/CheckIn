from fastapi import FastAPI
from model import Student, Course, Teacher
from db.course_db import courseDatabase
from db.student_db import StudentDatabase
from db.teacher_db import teacherDatabase
from db.roll_call_db import RollCallDatabase

app = FastAPI()

course_db = courseDatabase("CheckIn.db")
student_db = StudentDatabase("CheckIn.db")


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
    course_id = course_db.create_course(course_info)
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
    success = course_db.edit_course(course_info)
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
    success = course_db.delete_course(id)
    return {"success": "success" if success else "fail"}


@app.get("/course/list", tags=["course"], summary="List courses")
def list_course():
    """
    TODO
    output: course_list
    """
    course_list = course_db.list_courses()
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
    student_list = course_db.list_students(id)
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


@app.patch("/student/{studentID}/{courseID}", tags=["student"], summary="Assign course")
def assign_course():
    """
    TODO
    input: student_id, course_id
    output: success/fail
    """
    success = roll_call_db.assign_course(studentID, courseID)
    return {"success": success}


@app.post("/student/{studentID}/{courseID}/roll-call", tags=["student"], summary="Roll call")
def roll_call():
    """
    TODO
    input: student_id, course_id
    output: success/fail
    """
    success = roll_call_db.roll_call(studentID, courseID)
    return {"success": success}


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
    result = roll_call_db.roll_call_history(studentID)
    return {"roll_call_history": result}


@app.post("/teacher", tags=["teacher"], summary="Create teacher")
def create_teacher(teacher: Teacher):
    """
    TODO
    input: teacher_info
    output: teacher_id
    """
    teacher_info = teacher.model_dump()
    teacher_id = teacher_db.create_teacher(teacher_info)
    return {"teacher_id": teacher_id}


@app.patch("/teacher/{teacherID}", tags=["teacher"], summary="Edit teacher")
def edit_teacher(teacherID: int, teacher: Teacher):
    """
    TODO
    input: teacher_id, teacher_info
    output: success/fail
    """
    teacher_info = teacher.model_dump()
    if teacherID != teacher_info["id"]:
        return {"message": "teacherID does not match teacher info"}
    success = teacher_db.edit_teacher(teacher_info)
    return {"success": "success" if success else "fail"}


@app.delete("/teacher/{teacherID}", tags=["teacher"], summary="Delete teacher")
def delete_teacher(teacherID: int, teacher: Teacher):
    """
    TODO
    input: teacher_id
    output: success/fail
    """
    id = teacher.model_dump()["id"]
    if teacherID != id:
        return {"message": "teacherID does not match teacher info"}
    success = teacher_db.delete_teacher(id)
    return {"success": "success" if success else "fail"}
