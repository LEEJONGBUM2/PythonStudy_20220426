# 클래스 이름 -> 첫글자가 대문자, 카멜표기법
# 클래스 내부(속성, 기능)(변수, 함수) ctrl+f5가 실행 단축키이다.

class Student:
    name = ""
    schoolName = ""
    studentYear = 0

    def showInfo(self): #s1.showInfo가 showinto(self)에 들어간다
        print(f"학생이름:  {self.name}") #클래스 안에 있는 함수들을 메소드라고 부른다.
        print(f"학교명: {self.schoolName}")
        print(f"학년: {self.studentYear}")
        print()


s1 = Student()
s2 = Student()

print(id(s1)) #주소값 생성
print(id(s2))

s1.name = "김준일"
s2.name = "김준이"

s1.schoolName = "부산대학교"
s2.schoolName = "부경대학교"

s1.studentYear = 1
s2.studentYear = 4

s1.showInfo()
s2.showInfo()