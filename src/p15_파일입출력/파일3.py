f = open('src/p15_파일입출력/hello.txt', 'a', encoding='utf8')
f.write('글을 추가합니다.\n')
f.close()

f = open('src/p15_파일입출력/hello.txt', 'r', encoding='utf8')

print(f.read())

f.close()

with open('src/p15_파일입출력/hello.txt', 'r', encoding='utf8') as f:
    print(f.read())

#print(f.read()) 들여쓰기 밖에서는 file객체를 쓸 수 없다.
