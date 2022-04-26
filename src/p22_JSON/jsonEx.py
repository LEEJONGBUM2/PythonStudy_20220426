import json

user_json = '''{
    "company" : "kakao",
    "users" : [
        {
        "usercode" : "20220001",
        "username" : "jongbum",
        "password" : "1234",
        "name" : "이종범",
        "email" : "cjdrh2@naver.com"
        },{
        "usercode" : "20220002",
        "username" : "jongbum2",
        "password" : "12345",
        "name" : "이종범이",
        "email" : "cjdrh3@naver.com"
        }
    ]
}'''

user_json_obj = json.loads(user_json) #json 형태를 loads 형태를 바꿀땐 python을 사용한다.

print(user_json_obj)
print(type(user_json_obj)) #class dict
print(f'회사명: {user_json_obj.get("company")}')
userList = user_json_obj.get("users")
print(f'첫번째 사원의 정보: {userList[0].get("name")}')
print(f'두번째 사원의 정보: {userList[1].get("name")}')
