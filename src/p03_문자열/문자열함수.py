#count함수
name = "김준일김"

nameStrCount = name.count('김')

print(f"문자 김의 개수: {nameStrCount}")

#find함수
address = "창원시 동래구 사직동 중앙대로"
print("find")
cityIndex = address.rfind("시")
print(address[:cityIndex+1])
#index함수
print("index")
cityIndex = address.rindex("시")
print(address[:cityIndex+1])

guIndex = address.rfind("구")
dongIndex = address.rfind("동")

print(address[cityIndex + 2:guIndex+1])
print(address[guIndex + 2:dongIndex+1])

#join함수(문자열 삽입)
name = "김준일"
nameJoin = "r".join(name)
print(nameJoin)

#upper(대문자변환)
str1 = "Junil"
print(str1.upper())

#lower(소문자변환)
str2 = str1.upper()
print(str2.lower())

#strip(공백제거)
username = " skjil1218 "
lstripUsername = username.lstrip()
print("000" + lstripUsername + "000")

rstripUsername = username.rstrip()
print("000" + rstripUsername + "000")

stripUsername = username.strip()
print("000" + stripUsername + "000")

#replace(문자열 바꾸기)
phoneNumber = "010-9988-1916"
replacePhone = phoneNumber.replace("-", "")
replacePhone = replacePhone.replace(" ", "")
print(replacePhone)
