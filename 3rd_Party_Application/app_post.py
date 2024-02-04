import requests     # pip install requests
import json

URL = "http://127.0.0.1:8000/api/list/"     # Django----app/urls.py--->

data = {
    "username":"JaiPatel",                  # "model_col_name":"value" or "serializer_field_name":"value".
    "first_name":"Jai",                     # "fixed":"variable".
    "last_name":"Patel",
    "email":"Jai@gmail.com",
    "password":"jai@123"
}

json_data = json.dumps(data)
# print(json_data)
r = requests.post(url=URL,data=json_data)   # requests.post(argu1,argu2)--argu1 is used for url and argu2 is used for send data
data1 = r.json()
print(data1)