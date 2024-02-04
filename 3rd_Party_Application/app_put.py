import requests
import json

URL = "http://127.0.0.1:8000/api/list/"
data = {
    'id': 2,
    "username":"VishnuPatel",
    "first_name":"VishnuPatel",
    "password":"vis@123"
    }
json_data = json.dumps(data)
r = requests.put(url = URL, data = json_data)
data = r.json()
print(data)