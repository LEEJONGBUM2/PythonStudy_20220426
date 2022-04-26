# 이메일: (email)
# 성명: (name)
# 사용자이름:   (username)
# 비밀번호: (password)

userList = list()

i = 0

while i < 2:
    user = dict()
    email = input('이메일: ')
    name = input('성명: ')
    username = input('사용자이름: ')
    password = input('비밀번호: ')

    user['email'] = email
    user['name'] = name
    user['username'] = username
    user['password'] = password

    userList.append(str(user))
    userList.append('\n')
    i += 1

print(userList)

with open('src/p15_파일입출력/user.txt', 'w', encoding='utf8') as f:
    f.writelines(userList)


    