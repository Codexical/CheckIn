from pydantic import BaseModel


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
