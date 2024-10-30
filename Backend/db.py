import sqlite3


class Database:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.con.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute(
                "create table if not exists students(name, school, gender, phone, class_num)"
            )
            self.con.commit()
        except Exception as err:
            print(err)
            return False
        return True

    def insert_data(self, name, school, gender, phone, class_num):
        try:
            self.cursor.execute(
                "insert into students values("
                + f"'{name}', "
                + f"'{school}', "
                + f"'{gender}', "
                + f"'{phone}', "
                + f"{class_num})"
            )
            self.con.commit()
        except Exception as err:
            print(err)
            return False

        return True
