import sqlite3


class teacherDatabase:
    def __init__(self, db_name: str) -> None:
        self.con = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.con.cursor()

        try:
            self.cursor.execute(
                "create table if not exists teachers("
                + "teacher_id integer primary key,"
                + "name text,"
                + ")"
            )
            self.con.commit()
        except Exception as err:
            print(f"Courses table creation failed: {err}")

    def create_teacher(self, teacher_info) -> int:
        name = teacher_info["name"]
        try:
            self.cursor.execute("select count(*) from teachers")
            teacher_id = self.cursor.fetchone()[0] + 1

            self.cursor.execute(
                "insert into teachers values(" + f"{teacher_id}, " + f"'{name}')"
            )
            self.con.commit()
            return teacher_id
        except Exception as err:
            print(f"Teacher creation failed: {err}")
            return -1

    def edit_teacher(self, teacher_info) -> bool:
        teacher_id = teacher_info["id"]
        name = teacher_info["name"]
        try:
            self.cursor.execute(
                "update teachers set "
                + f"name='{name}' "
                + f"where teacher_id={teacher_id}"
            )
            self.con.commit()
            return True
        except Exception as err:
            print(f"Teacher edit failed: {err}")
            return False

    def delete_teacher(self, teacher_id: int) -> bool:
        try:
            self.cursor.execute(f"delete from teachers where teacher_id={teacher_id}")
            self.con.commit()
            return True
        except Exception as err:
            print(f"Teacher deletion failed: {err}")
            return False

    def list_teachers(self) -> dict:
        try:
            self.cursor.execute("select * from teachers")
            teachers = self.cursor.fetchall()
            return teachers
        except Exception as err:
            print(f"Teacher listing failed: {err}")
            return []
