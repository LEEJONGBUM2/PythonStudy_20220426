import json

class DataBase: #데이터를 불러오고 데이터를 저장하기 위한 것이다. #파일이 없으면 파일을 만들라는 의미이다.
    data = {
        "user_mst": list()
    }

    def __init__(self):
        try:
            with open("./src/UserManagement/userdata.json", "r", encoding="utf8") as f:
                self.data = json.load(f)
        except FileNotFoundError: #만약 파일을 찾지 못하면 새파일을 만들어라
            with open("./src/UserManagement/userdata.json", "w", encoding="utf8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
            with open("./src/UserManagement/userdata.json", "r", encoding="utf8") as f:
                self.data = json.load(f)

    def getData(self):
        return self.data

    def save(self):
        # print(self.data)
       with open("./src/UserManagement/userdata.json", "w", encoding="utf8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

