n = int(input("별의 개수: "))
i = 0
while i < n:
    i += 1
    print(" " * (n - i), end='')
    print("*" * i)
    
i = 0
while i < n:
    print((" " * i) + ("*" * (n - i)))
    i += 1