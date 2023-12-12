#11.	Write a python program to find first and last digit of a number
num = int(input("enter any number"))
count=0
while(num!=0):
    if(count==0):
        last = num%10
        count = count + 1
    first = num%10
    num = num//10
print("first digit are: ",first)
print("last digit are: ",last)