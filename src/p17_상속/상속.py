class ClassA:
    num = 0

    def __init__(self):
        print("부모클래스 생성")

    def setNum(self, num):
        self.num = num

    def getNum(self):
        return self.num    

    def printlnfo(self):
        print("A클래스 정보")


class ClassB(ClassA): #상속을 받았기 때문이다.
    def __init__(self):
        print("자식 클래스 생성")

b = ClassB()
b.printlnfo()
b.setNum(10000)
print(b.getNum())
b.num = 20000
print(b.num)
print(b.getNum())

