from fastapi import FastAPI
from pydantic import BaseModel
from db import Database

app = FastAPI()

db = Database("students.db")


class Item(BaseModel):
    name: str
    school: str
    gender: str
    phone: str
    class_num: int


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/create-table")
def create_table():
    result = create_table
    if not result:
        return {"message": "Fail, check data"}
    return {"message": "Success"}


@app.post("/insert-student")
def insert_db(item: Item):
    item_dict = item.dict()
    result = db.insert_data(
        item_dict["name"],
        item_dict["school"],
        item_dict["gender"],
        item_dict["phone"],
        item_dict["class_num"],
    )

    if not result:
        return {"message": "Fail, check data"}
    return {"message": "Success"}


@app.post("/course/create", tags=["course"])
def create_course():
    """ 
    TODO 
    input: course_info
    output: course_id
    """


@app.post("/course/edit", tags=["course"])
def edit_course():
    """ 
    TODO 
    input: course_id, course_info
    output: success/fail
    """


@app.post("/course/delete", tags=["course"])
def delete_course():
    """ 
    TODO 
    input: course_id
    output: success/fail
    """


@app.get("/course/list", tags=["course"])
def list_course():
    """ 
    TODO 
    output: course_list
    """


@app.post("/course/students", tags=["course"])
def list_students():
    """ 
    TODO 
    input: course_id
    output: student_list
    """


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
