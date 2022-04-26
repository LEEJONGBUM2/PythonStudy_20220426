#자동차
"""
    company
    model
    color

    showCarInfo()
        제조사: 현대자동차
        모델: 쏘나타
        색상: 화이트
"""

class Car: #클래스는 속성(변수)와 기능(메소드)로 이루어져 있다.
    company= ""
    model= ""
    color= ""

    def __init__(self): #line34를 통해서 호출이 된다.
        print("생성자 호출됨?")

    # def __init__(self, str):
    #     print("두번째 생성자 호출됨?")
    #     print(f"str: {str}")

    def showCarInfo(self): #
        print(f"제조사: {self.company}")
        print(f"모델: {self.model}")
        print(f"색상: {self.color}")
        print()

    # def showCarInfo(self, str1): #메소드 오버로딩
    #     print(str1)

    # def showCarInfo(self, str1):
    #     print(str1)

    def test(self, *args): #모든 매개변수는 self가 들어가야 된다.
        for arg in args:
            #print(type(arg))
            if str(type(arg)) == "<class 'int'>":
                print(f'정수: {arg}')
            elif str(type(arg)) == "<class 'str'>":
                print(f'문자열: {arg}')


c1 = Car() #주소(Car)를 변수에다가 담았다.

#c2 = Car("두번째 자동차를 생산합니다.")
# print(id(c1))
#Car()
c1.company = "현대자동차"
c1.model = "쏘나타"
c1.color = "화이트"

c1.showCarInfo()
#c1.showCarInfo("test")
print(c1.company)

c1.test(1,2,3,"4",5,6)
#c1.showCarInfo("현대자동차, 쏘나타, 화이트")

