class 아부지:
    carModel = ""
    carColor = ""

    def showCarInfo(self):
        self.carColor = "화이트"
        print("[차량정보]")
        print(f"차량 모델: {self.carModel}")
        print(f"차량 색상: {self.carColor}")

class 자식(아부지):
    def showCarInfo(self): #화이트에 대한것을 재정의 했다.
        self.carColor = "블랙"
        print("[차량정보]")
        print(f"차량 모델: {self.carModel}")
        print(f"차량 색상: {self.carColor}")

준일 = 자식()
준일.carModel = "쏘나타"
준일.showCarInfo()