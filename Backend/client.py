"""
A single program to test POST result.
"""

import requests
import json
import time

param={
    "name": "Yi",
    "school": "NPTU",
    "gender": "男",
    "phone": "0987654321",
    "class_num": "3"
}

url='http://127.0.0.1:8080/insert-student'

html = requests.post(url, json.dumps(param))

print(html.text)