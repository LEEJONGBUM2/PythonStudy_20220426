import json

json_data = '''{
    "username":"jongbum",
    "password":"1234"
}
'''

user_data = json.loads(json_data)
print(user_data)
print(type(user_data))
print(user_data.get("username"))

with open("./src/p22_JSON2/userdata.json", "w", encoding="utf8") as f: #userdata.json을 만들수가 있다.
    json.dump(user_data, f, indent=2, ensure_ascii=False)

with open("./src/p22_JSON2/userdata.json", "r", encoding="utf8") as f:
    user_data = json.load(f)

print(user_data)

user_data_str = json.dumps(user_data, indent=4)
print(user_data_str)
print(type(user_data_str))