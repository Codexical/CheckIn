import sqlite3


class Database:
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

    # def create_table(self):
    #     try:
    #         self.cursor.execute(
    #             "create table if not exists students(name, school, gender, phone, class_num)"
    #         )
    #         self.con.commit()
    #     except Exception as err:
    #         print(err)
    #         return False
    #     return True

    # def insert_data(self, name, school, gender, phone, class_num):
    #     try:
    #         self.cursor.execute(
    #             "insert into students values("
    #             + f"'{name}', "
    #             + f"'{school}', "
    #             + f"'{gender}', "
    #             + f"'{phone}', "
    #             + f"{class_num})"
    #         )
    #         self.con.commit()
    #     except Exception as err:
    #         print(err)
    #         return False

    #     return True
