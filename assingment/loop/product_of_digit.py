# 14.Write a python program to calculate product of digits of a number.
num = int(input("enter any number"))
prod=1
while(num>0):
    dig = num%10
    prod= prod*dig
    num = num//10
print("product is: ",prod)