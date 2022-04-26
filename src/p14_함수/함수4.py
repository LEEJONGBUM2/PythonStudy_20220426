def namesAndphones(names, phones):
    namesStr = "||".join(names)
    phonesStr = "||".join(phones)
    return namesStr, phonesStr

names = ["김준일", "송지한", "이건용", "이영현", "전주홍"]
phones = ["010-9988-1916", "010-9988-1917", "010-9988-1918", "010-9988-1919", "010-9988-1919"]
result = namesAndphones(names, phones)
result1, result2 = namesAndphones(names, phones)
print(result)
print(result1)
print(result2)