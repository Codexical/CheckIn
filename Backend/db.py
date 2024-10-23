import sqlite3

con = sqlite3.connect('database/student_info.db', check_same_thread=False)
cursorObj = con.cursor()

def create_table():
    try:
        cursorObj.execute("create table if not exists students(name, school, gender, phone, class_num)")
    except Exception as err:
        print(err)
        return False
    
    return True


def insert_data(name, school, gender, phone, class_num):
    try:
        cursorObj.execute(
            "insert into students values("
            + f"'{name}', "
            + f"'{school}', "
            + f"'{gender}', "
            + f"'{phone}', "
            + f"{class_num})")
    except Exception as err:
        print(err)
        return False
    
    return True

con.commit()