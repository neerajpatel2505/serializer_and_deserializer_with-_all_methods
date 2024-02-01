import requests
import json

URL = "http://127.0.0.1:8000/api/list/"
data = {
    'id': 2,
    "username":"VishnuPratapPatel",
    "first_name":"Vishnu",
    "last_name":"Patel",
    "email":"Vishnu@gmail.com",
    "password":"vis@123"
    }
json_data = json.dumps(data)
r = requests.put(url = URL, data = json_data)
data = r.json()
print(data)