def factorial(x):
    s=1
    while x!=0:
       s= s*x
       x-=1
    print(s)
b= int(input("Enter the number"))
print("The factorial is ",end="")
factorial(b)