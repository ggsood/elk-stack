import requests
import json

r = requests.get("https://randomuser.me/api/")
# json_data = json.loads(r.content)
print(r.content)
# for item in json_data:
#     print(item)
