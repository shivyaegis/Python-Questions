import math
a = int(input("enter side a "))
b = int(input("enter side b "))
c = int(input("enter side c "))
s = (a+b+c)/2
print(s)
x = s
y = s - a
z = s - b
ar = (x*y*z)
area = math.sqrt(ar)
print ("area is " ,area)