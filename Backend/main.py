from fastapi import FastAPI
from pydantic import BaseModel

import db

app = FastAPI()


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
        item_dict['name'],
        item_dict['school'],
        item_dict['gender'],
        item_dict['phone'],
        item_dict['class_num']
    )

    if not result:
        return {"message": "Fail, check data"}
    return {"message": "Success"}