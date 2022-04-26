class User:
    email = ""
    name = ""
    username = ""
    password = ""


    def toString(self):
        return """[UserData]
email: {self.email}
name: {self.name}
username: {self.username}
"""
        # print("")
        # print(f"email: {self.email}")
        # print(f"name: {self.name}")
        # print(f"username: {self.username}")

    def toDict(self):
        userDict = dict()
        userDict["email"] = self.email
        userDict["name"] = self.name
        userDict["username"] = self.username
        userDict["password"] = self.password
        return userDict