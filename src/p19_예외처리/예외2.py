number = -1

try:
    if number > 0:
        pass
    elif number == -1:
        list1 = [1,2,3,4,5]
        list1.index(6)
    else:
        raise FileNotFoundError
#except RuntimeError as e: #as는 대체 하는 것을 의미한다.
except ValueError as e:
    print(f"오류 내용: {e}") # 6 is not in list

except IndexError as e:
    print(f"오류 내용: {e}")
except FileNotFoundError as e:
    print(f"오류 내용: {e}")
except Exception as e: #as는 대체 하는 것을 의미한다. #Exception은 제일 밑에 출력을 한다.
    import traceback
    traceback.print_exc() #traceback import를 해서 예외내용을 출력하게 도와준다.
    #print(f"오류 내용: {e}")
else:
    print("오류가 발생하지 않으면 실행")
finally:
    print("무조건 실행") #예외 발생 유무에 상관하지 않고 저장이된다 finally

print("프로그램 종료")