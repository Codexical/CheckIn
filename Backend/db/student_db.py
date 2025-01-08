import sqlite3


class StudentDatabase:
    def __init__(self, db_name: str) -> None:
        self.con = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute(
                "create table if not exists students("
                + "name text,"
                + "course_id integer,"
                + "birth text,"
                + "school_name text,"
                + "school_grade text,"
                + "parent_name text,"
                + "mobile text,"
                + "phone text"
                + ")"
            )
            self.con.commit()
        except Exception as err:
            print(f"Students table creation failed: {err}")


    def create_student(self, student_info) -> int:
        name = student_info["name"]
        course_id = student_info["course_id"]
        birth = student_info["birth"]
        school_name = student_info["school_name"]
        school_grade = student_info["school_grade"]
        parent_name = student_info["parent_name"]
        mobile = student_info["mobile"]
        phone = student_info["phone"]
        try:
            self.cursor.execute(
                "insert into students values("
                + f"'{name}', "
                + f"{course_id}, "
                + f"'{birth}', "
                + f"'{school_name}', "
                + f"'{school_grade}', "
                + f"'{parent_name}', "
                + f"'{mobile}', "
                + f"'{phone}')"
            )
            self.con.commit()
            self.cursor.execute("select last_insert_rowid() from students")
            id = self.cursor.fetchone()
            return id[0]
        except Exception as err:
            print(f"Student creation failed: {err}")
            return -1


    def edit_student(self, student_info, id: int) -> bool:
        name = student_info["name"]
        course_id = student_info["course_id"]
        birth = student_info["birth"]
        school_name = student_info["school_name"]
        school_grade = student_info["school_grade"]
        parent_name = student_info["parent_name"]
        mobile = student_info["mobile"]
        phone = student_info["phone"]
        try:
            self.cursor.execute(
                "update students set "
                + f"name='{name}', "
                + f"course_id={course_id}, "
                + f"birth='{birth}', "
                + f"school_name='{school_name}', "
                + f"school_grade='{school_grade}', "
                + f"parent_name='{parent_name}', "
                + f"mobile='{mobile}', "
                + f"phone='{phone}' "
                + f"where rowid={id};"
            )
            self.con.commit()
            return True
        except Exception as err:
            print(f"Student edit failed: {err}")
            return False


    def delete_student(self, id: int) -> bool:
        try:
            self.cursor.execute(f"delete from students where rowid={id}")
            self.con.commit()
            return True
        except Exception as err:
            print(f"Student deletion failed: {err}")
            return False


    def list_courses(self) -> list:
        try:
            self.cursor.execute("select * from students")
            courses = self.cursor.fetchall()
            print(courses)
            return courses
        except Exception as err:
            print(f"Course listing failed: {err}")
            return []