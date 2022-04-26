#from 사칙연산 import sum, div
from unicodedata import name
import 사칙연산 as a
#알리야스 -> 별명

#print(sum(10, 20, 30, 40))
print(a.sum(10, 20, 30, 40))

#print(div(100, 20, 2))
print(a.div(100, 20, 2))

print(a.getName())
print(a.__name__)

def sum(num, num2):
    return num + num2

name = input("사용할 모듈을 입력하세요: ")

if a.__name__ == name :
    print(a.sum(10, 20))
elif __name__ == name :
    print(sum(50, 20))

# class A:
#     def __init__(self) -> None:
#         pass