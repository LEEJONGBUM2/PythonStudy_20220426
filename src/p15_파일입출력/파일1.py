#
# 절대경로(경로 맨 앞에 / 또는 \로 시작하는 것)

# 상대경로(./ 또는 ../ 또는 생략 으로 시작하는 것)
#
from asyncore import write


strList = ['이름: 김준일\n', '나이: 29\n', '주소: 부산 동래구\n']

f = open('src/p15_파일입출력/hello.txt', 'w', encoding='utf8')
f.writelines(strList)
for string in strList:
    f.write(string)
f.close()