result = 0
i = 1

while i < 1001:
    if i % 3 == 0:
        result = result + i
    i = i + 1

print(result)

result = 0

for i in range(1, 1001):
    if i % 3 == 0:
        result = result + i
print(result)

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
avg = 0
for i in score:
    total = total + i
avg = total / len(score)

print(f"평균: {avg}")