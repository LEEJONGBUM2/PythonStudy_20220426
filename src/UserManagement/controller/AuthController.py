import os
import time
class AuthController:
    userService = None
    principalUser = None
    
    def __init__(self, userService):
        self.userService = userService

    def index(self):
        while True:
            os.system('cls') #콘솔창을 클리어하는 역할을 한다.
            print("[사용자 관리 프로그램]")
            print("1. 회원가입")
            print("2. 로그인")
            print("q. 프로그램 종료")
            select = input("명령을 선택하세요: ")

            if select == "1":
                self.userService.signup()
            elif select == "2":
                self.principalUser = self.userService.signin()
                if self.principalUser == None:
                    select = input("로그인에 실패하였습니다. \n다시 로그인 하시겠습니까?(y/n): ")
                    if select != "y":
                        self.exit()
                        break
                else:
                    self.mypage()
            elif select == "q":
                print("프로그램 종료중...")
                for i in range(100):
                    os.system('cls')
                    print(f"{i+1} / 100")
                    time.sleep(0.05)
                break
            else:
                print("배당 명령은 지원하지 않습니다.")

        print("프로그램이 종료 되었습니다.")

    def mypage(self):
        while True:
            os.system('cls') #콘솔창을 클리어하는 역할을 한다.
            print(f"[마이페이지({self.principalUser.get('username')})]")
            print("1. 전체 사용자 조회")
            print("2. 프로필 내용 조회")
            print("b. 로그아웃")
            select = input("명령을 선택하세요: ")

            if select == "1":
                self.userService.showUserAll()
                self.next()
            elif select == "2":
                print("[프로필 내용 조회]")
                self.userService.printUser(self.principalUser)
                self.next()
                # print(
                #     f"""이메일: {self.principalUser.get('email')}
                #     이름: {self.principalUser('name')}
                #     아이디: {self.principalUser('username')}"""
                # )
                # print(self.principalUser.toString())
            elif select == "b":
                self.principalUser = None
                break
            else:
                print("배당 명령은 지원하지 않습니다.")

    def next(self):
        input("계속하시려면 아무키나 입력하세요: ")

    # def exit(self):
    #     print("프로그램 종료중...")
    #     for i in range(100):
    #         os.system('cls')
    #         print(f"{i+1} / 100")
    #         time.sleep(0.01)
