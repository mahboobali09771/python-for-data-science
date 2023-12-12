'''2 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
Ex   Input :    beautiful           Expected Output : beul
'''
st = "beautiful"
st1 = st[0:2] + st[-2:len(st)]
print(st1)