list1 = [1,2,3,4,5,6,7,8,9]
list2 = [i for i in list1]
print(list2)

list3 = [i + 1 for i in list1]
print(list3)

list4 = [i for i in list1 if i % 2 == 0]
print(list4)