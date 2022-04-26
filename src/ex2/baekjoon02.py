x, y = map(int, input("x축과 y축을 입력하세요: ").split(','))

if x == 0 and y == 0:
    print("원점")
elif x > 0 and y > 0:
    print("1사분면")
elif x < 0 and y > 0:
    print("2사분면")
elif x < 0 and y < 0:
    print("3사분면")
else:
    print("4사분면")