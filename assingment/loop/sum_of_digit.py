#13.Write a python program to calculate sum of digits of a number.
num = int(input("enter any number"))
sum=0
while(num>0):
    dig = num%10
    sum= sum+dig
    num = num//10
print("sum is: ",sum)
    
    

   

