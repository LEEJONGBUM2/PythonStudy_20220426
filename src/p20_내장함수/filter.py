def phoneNumberCheck(x):
    x = x[:x.find("-")]
    return x in ["010", "011", "016", "017", "02", "051"]

phoneNumber = ["010-5133-4268", "011-1234-4567", "02-456-7890", "012-111-2222"]
print(list(filter(phoneNumberCheck, phoneNumber)))