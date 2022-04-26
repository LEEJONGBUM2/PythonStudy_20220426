from unittest import result

def getName():
    return __name__

def sum(*args):
    result = 0
    for num in args:
        result += num
    return result

def sub(*args):
    result = args[0] * 2 # args[0]은 100이라는 의미 200-100-20-30=50
    for num in args:
        result -= num
    return result

#sub(100, 20, 30)

def mul(*args):
    result = 1
    for num in args:
        result *= num
    return result

def div(*args):
    result = args[0] * args[0]
    if 0 in args:
        return 0
    for num in args:
        result /= num
    return result

print(f'실행위치 {__name__}')

if __name__ == "__main__":
    print("현재 name이 main입니다.")

print("사칙연산 모듈")

print(mul(10, 2))