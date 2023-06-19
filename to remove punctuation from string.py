str2 = ''
str_r = ":",";","!","?","'","'","@","&"
str1 = str(input("enter a string "))
for i in str1:
    if i in str_r:
        continue
    else:
        str2 += i
print(str2)