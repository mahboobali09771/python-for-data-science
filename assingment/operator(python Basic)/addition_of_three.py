#5.	Write a Python program that read a 3 digit number from user and perform the addition of their digits.
n = int(input("enter three digit number"))
sum=0
while(n>0):
    i= n%10
    sum += i
    n = n//10
print(sum)
