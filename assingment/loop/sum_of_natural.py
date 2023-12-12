#6.	Write a python program to find sum of all natural numbers between 1 to n
n = int(input("enter any  number: "))
sum=0
while(n>0):
    sum = sum+n
    n -= 1
print(sum)
 