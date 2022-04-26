# 변수 score <- 입력
# score가 0보다 작거나 100보다 크면 해당 점수는 계산할 수 없습니다.
# 아니라면 A,B,C,D,F 학점을 계산하여 출력


score = int(input("점수를 입력해주세요: "))

if score > 100 or score < 0:
    print("해당 점수는 계산할 수 없습니다.")
elif score > 89:
    print("A학점")
elif score > 79:
    print("B학점")
elif score > 69:
    print("C학점")
elif score > 59:
    print("D학점")
else:
    print("F학점")

