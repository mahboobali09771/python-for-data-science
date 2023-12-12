#6.	Write a python program to find the greatest number among three.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number :"))

if(a>b and a>c):
    print("a is greatest")
elif(b>c and b>a):
    print("b is greatest")
else:
    print("c is greatest")
