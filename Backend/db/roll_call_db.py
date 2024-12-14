import sqlite3
import time


class RollCallDatabase:
    def __init__(self, db_name: str) -> None:
        self.con = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.con.cursor()

        try:
            self.cursor.execute(
                f"create table if not exists assign("
                + "course_id integer,"
                + "course_name text,"
                + "teacher_id integer,"
                + "course_time text,"
                + "student_id integer,"
                + "student_name text,"
                + "roll_call integer" # 0 means not roll call yet
                + ")"
            )
            self.con.commit()
        except Exception as err:
            print(f"Courses table creation failed: {err}")

    def assign_course(self, student_id, course_id) -> bool:
        try:
            self.cursor.execute(f"select * from students where rowid={student_id}")
            student_info = self.cursor.fetchall()
            self.cursor.execute(f"select * from courses where course_id={course_id}")
            course_info = self.cursor.fetchall()

            self.cursor.execute(
                f"insert into table assign values("
                + f"{course_id},"
                + f"{course_info[1]},"
                + f"{course_info[2]},"
                + f"{course_info[3]},"
                + f"{student_id},"
                + f"{student_info[0]},"
                + "0"
                + ")"
            )
            self.con.commit()
            return True
        except Exception as err:
            print(f"Assign Course failed: {err}")
            return False
    def roll_call(self, student_id, course_id) -> bool:
        try:
            self.cursor.execute(f"select * from assign where student_id={student_id} ans course_id={course_id}")
            roll_call_info = self.cursor.fetchall()
            roll_call_info[6] = 0 if roll_call_info[6] == 1 else 1
            self.cursor.execute(
                f"update assign set("
                + f"course_id='{roll_call_info[0]}',"
                + f"course_name='{roll_call_info[1]}',"
                + f"teacher_id='{roll_call_info[2]}',"
                + f"course_time='{roll_call_info[3]}',"
                + f"student_id='{roll_call_info[4]}',"
                + f"student_name='{roll_call_info[5]}',"
                + f"roll_call='{roll_call_info[6]}'" # 0 means not roll call yet
                + ")"
            )
            self.con.commit()
            return True
        except Exception as err:
            print(f"Roll call failed: {err}")
            return False
    def roll_call_history(self, student_id) -> list:
        try:
            self.cursor.execute(f"select * from assign where student_id={student_id}")
            student_roll_call_info = self.cursor.fetchall()
            return student_roll_call_info
        except Exception as err:
            print(f"Roll call history fetch failed: {err}")
            return []