#from UserManagement.repository.user.User import AuthController
from controller.AuthController import AuthController
from service.UserService import UserService
from repository.UserRepository import UserRepository
from repository.DataBase import DataBase



dataBase = DataBase()
userRepository = UserRepository(dataBase)
userService = UserService(userRepository)
authController = AuthController(userService)
authController.index()


# user1 = User()
# user1.email = "jongbum@kakao.com"
# user1.name = "이종범"
# user1.username = "jongbum"
# user1.password = "1234"

# print(user1.toString())

# print(user1.toDict())
####
# dict 값찾기[]