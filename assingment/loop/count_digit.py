# 10.	Write a python program to count number of digits in a number
n = int(input("enter any digit"))
count=0
while(n>0):
    i=n%10
    count=count+1
    n= n//10
print(count)