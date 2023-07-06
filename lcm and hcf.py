num1 = int(input("enter number 1 "))
num2 = int(input("enter number 2 "))
a = num1
b = num2
while b !=0:
    t = b
    b = a % b
    a = t
hcf = a
lcm = (num1 * num2)/hcf
print("hcf is" , hcf)
print("lcm is" , lcm)