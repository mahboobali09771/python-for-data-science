#8.	Enter basic salary from the user. Write a program to calculate DA and HRA on the following conditions:-
'''
Salary      	  DA	HRA
<=2000	         10%	20%
>2000 && <=5000	 20%	30%
>5000 && <=10000 30%	40%
>10000	         50%	50%
'''

salary = int(input("enter basic salary"))
if(salary<=2000):
    da=(salary*10)/100
    hra=(salary*20)/100
    print(da)
    print(hra)
elif(salary>2000 and salary<=5000):
    da=(salary*20)/100
    hra=(salary*30)/100
    print(da)
    print(hra)
elif(salary>5000 and salary<=10000):
     da=(salary*30)/100
     hra=(salary*40)/100
     print(da)
     print(hra)
elif(salary>10000):
     da=(salary*50)/100
     hra=(salary*50)/100
     print(da)
     print(hra)
     print("enter valid salary")


    