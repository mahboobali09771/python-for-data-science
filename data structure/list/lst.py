lst=[[56,56,79],[23,56,89],33,89,20]
for i in lst:
    if type(i)==list:
        for j in i:
            if j%2==0:
                print(j)
    else:
        if i%2==0:
            print(i)