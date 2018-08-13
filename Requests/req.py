import requests
import json


r = requests.get("https://reqres.in/api/users?page=2")
rjson = r.json()

print(r.status_code)
print(rjson["data"][0]["id"])

for r in rjson["data"]:
    print(r["id"])
    print(r["first_name"])


