for i in range(0,4):
    for j in range(0,7):
        if (j-i)>= 4:
            print(' ',end='')
        elif (i+j)<= 2:
            print(' ',end='')
        else:
            if (i+j)%2 == 0:
               print('*',end='')
            else:
                print(' ', end='')
    print()
