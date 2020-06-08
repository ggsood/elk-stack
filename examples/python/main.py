import requests
import json

payload = {
    "token": "NVGDxAYb0ykiXsKsg2XLKQ",
    "data": {
        "address": {
        "addressBuilding": "addressBuilding",
        "addressCity": "addressCity",
        "addressCountry": "addressCountry",
        "addressFullStreet": "addressFullStreet",
        "addressLatitude": "addressLatitude",
        "addressLongitude": "addressLongitude",
        "addressState": "addressState",
        "addressStateCode": "addressStateCode",
        "addressStreetName": "addressStreetName",
        "addressStreetSuffix": "addressStreetSuffix",
        "addressZipCode": "addressZipCode"
        },
        "email": "internetEmail",
        "gender": "personGender",
        "id": "personNickname",
        "last_login": {
        "date_time": "dateTime|UNIX",
        "ip4": "internetIP4"
        },
        "_repeat": 10
    },
    "parameters": {
        "code": 200
    }

};

r = requests.post("https://app.fakejson.com/q", json = payload)
json_data = json.loads(r.content)

# for item in json_data:
#     print(item)
