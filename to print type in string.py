str1 = (input("enter elements of string"))
for i in str1:
    if str(i).isalpha():
        print("alphabet")
    elif str(i).isnumeric():
        print("number")
    else:
        print("special character")