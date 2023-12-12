#8.	Write a python program to find sum of all odd numbers between 1 to n.
n = int(input("enter any number"))
sum=0
i=1
while(n>=i):
    if(i%2!=0):
        sum=sum+i
    i=i+1
print(sum)

# second method
'''
n = int(input("enter any number"))
sum=0
while(n>0):
    if(n%2!=0):
        sum=sum+n
    n = n-1
print(sum)
'''
