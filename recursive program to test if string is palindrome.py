str3 = ''
str2 = ''
a = str(input('enter a string'))
for i in (a):
    str2 += str(i)
print(str2)
for i in reversed(str2):
    str3 += str(i)
if str2 == str3:
    print("string is a palindrome",end='')
else:
    print("string is not a palindrome",end='')