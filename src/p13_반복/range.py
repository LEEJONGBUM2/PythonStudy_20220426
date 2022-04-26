list1 = range(2, 10)

for i in range(1, 11):
    print("*" * i)

for i in range(10, 0, -1):
    print("*" * i)

for i in range(0, 10):
    print((" " * (10 - 1 - i)) + ("*" * (i + 1)))

for i in range(10, 0, -1):
    print((" " * (10 - i)) + ("*" * i))

#     *
#    ***
#   *****
#  *******
# *********

for i in range(0, 5):
    print((" " * (5 - i - 1)) + ("*" * ((i * 2) + 1)))

for i in range(5, 0, -1):
    print((" " * (5 - i)) + ("*" * ((i * 2) - 1)))




 