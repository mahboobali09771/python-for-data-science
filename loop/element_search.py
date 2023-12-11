arr=[1,23,45,33,21,17]
num=int(input("enter a number to search"))
for i in arr:
    if i==num:
        print("number is in the list")
        break
else:
    print("number is not in the list")