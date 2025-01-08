import sqlite3


class courseDatabase:
    def __init__(self, db_name: str) -> None:
        self.con = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.con.cursor()

        try:
            self.cursor.execute(
                "create table if not exists courses("
                + "course_id integer primary key,"
                + "course_name text,"
                + "teacher_id integer,"
                + "course_time text"
                + ")"
            )
            self.con.commit()
        except Exception as err:
            print(f"Courses table creation failed: {err}")

    def create_course(self, course_info) -> int:
        course_name = course_info["course_name"]
        teacher_id = course_info["teacher_id"]
        course_time = course_info["course_time"]
        try:
            self.cursor.execute("select count(*) from courses")
            course_id = self.cursor.fetchone()[0] + 1

            self.cursor.execute(
                "insert into courses values("
                + f"{course_id}, "
                + f"'{course_name}', "
                + f"{teacher_id}, "
                + f"'{course_time}')"
            )
            self.con.commit()
            return course_id
        except Exception as err:
            print(f"Course creation failed: {err}")
            return -1

    def edit_course(self, course_info) -> bool:
        course_id = course_info["id"]
        course_name = course_info["course_name"]
        teacher_id = course_info["teacher_id"]
        course_time = course_info["course_time"]
        try:
            self.cursor.execute(
                "update courses set "
                + f"course_name='{course_name}', "
                + f"teacher_id={teacher_id}, "
                + f"course_time='{course_time}' "
                + f"where course_id={course_id}"
            )
            self.con.commit()
            return True
        except Exception as err:
            print(f"Course edit failed: {err}")
            return False

    def delete_course(self, course_id: int) -> bool:
        try:
            self.cursor.execute(f"delete from courses where course_id={course_id}")
            self.con.commit()
            return True
        except Exception as err:
            print(f"Course deletion failed: {err}")
            return False

    def list_courses(self) -> list:
        try:
            self.cursor.execute("select * from courses")
            courses = self.cursor.fetchall()
            print(courses)
            return courses
        except Exception as err:
            print(f"Course listing failed: {err}")
            return []

    def list_students(self, course_id: int) -> dict:
        try:
            self.cursor.execute(f"select * from students where course_id={course_id}")
            students = self.cursor.fetchall()
            return students
        except Exception as err:
            print(f"Student listing failed: {err}")
            return []
