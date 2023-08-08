for i in range(0,5):
    for j in range(0,9+i):
        while int(i) == 0 or 1 or 3 or 4:
            if int(j) == 3 or 4 or 5:
                print('*',end='')
        if int(i) == 2:
            print('*',end='')
        else:
            print('',end='')
    print()