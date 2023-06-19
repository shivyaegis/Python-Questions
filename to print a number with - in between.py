# to make program to print a number string as XXX - XXX - XXXX

str2 = ''
str1 = str(input("enter a string of 10 numbers"))
if len(str1) != 10:
    print("try again :/")
    str1 = ''
for i in range(0,len(str1)):
    if int(i) == 3 or int(i) == 6:
        str2 += '-'
        str2 += str1[i]
    else:
        str2+= str1[i]
print(str2)