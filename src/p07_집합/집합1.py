set1 = set([1,2,3,4,5])
print(set1)
set1.add(10)
set1.add(113)
set1.add(122)
set1.add(13)
set1.add(10)
set1.add(10)
set1.add(10)
set1.add(10)
set1.add(10)
set1.add(10)
set1.add(10)
set1.add(10)
set1.add(10)
print(set1)

set2 = set("안녕하세요")
print(set2)

search = '요'

list1 = list(set2)
print(list1[0])


for value in list1:
    if value == search :
        print(value)
        break


