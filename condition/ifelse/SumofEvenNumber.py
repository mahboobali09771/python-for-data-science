num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
if num1%2==0 and num2%2==0:
    res=num1 + num2
    print("sum of nums is: ",res)
    print("end of if")
else:
    print("only even nums are allowed")
print("end of code")