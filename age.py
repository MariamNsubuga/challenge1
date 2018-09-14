num = int(input("enter your year of birth"))
if num > 2000:
    print("your are minor")
elif (num > 2000  or num >= 1965):
    print("your are a youth")
else:
    print("your are an elder")