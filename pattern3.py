n = int(input("enter no of rows"))
m = int(input("enter no of columns"))
for i in range(0,n+1):
    for j in range(0,m+1):
        if (j-i)<0:
            print(j+1,end='')
        else:
            print('',end='')
    print()