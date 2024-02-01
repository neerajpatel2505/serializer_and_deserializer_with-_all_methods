import requests
import json

URL = "http://127.0.0.1:8000/api/list/"

data = {
    "username":"Arvind",
    "first_name":"Arvind",
    "last_name":"Patel",
    "email":"Arvind@gmail.com",
    "password":"arv@123"
}

json_data = json.dumps(data)
# print(json_data)
r = requests.post(url=URL,data=json_data)
data1 = r.json()
print(data1)