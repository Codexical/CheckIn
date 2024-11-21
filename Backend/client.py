"""
A single program to test POST result.
"""

import requests
import json
import time

param={
    "name": "Chovy",
    "course_id": 3,
    "birth": "1987/06/05",
    "school_name": "NPTU",
    "school_grade": "A",
    "parent_name": "你爸",
    "mobile": "0987654321",
    "phone": ""
}

url='http://127.0.0.1:8000/student/2'

html = requests.patch(url, json=param)

print(html.text)