# 2x1=2   2x2=4   2x3=6   2x9=18
# 3x1=3   3x2=6   3x3=9   3x9=27
# 9x1=9                   9x9=81

# print("2x2=4", end="\t")

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

