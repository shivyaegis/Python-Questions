def del_end(arr, n):
    if n == 0:
        print('\n'"array underflow... what am i supposed to remove!?")
    else:
        del arr[-1]
        print("\n", str(arr))


def del_front(arr, n):
    if n == 0:
        print('\n'"array underflow... what am i supposed to remove!?")
    else:
        z = 0
        while z < n-1:
            arr[z] = arr[z+1]
            z = z+1
        del arr[-1]
        print('\n', str(arr))


def del_loc(arr, n, loc):
    if n == 0:
        print('\n'"array underflow... what am i supposed to remove!?")
    elif loc > n:
        print("LOC>N invalid situation given...")
    else:
        for b in range(loc, n-1):
            arr[b] = arr[b+1]
        del arr[-1]
        print(arr)


def del_after(arr, n, ele):
    ind = arr.index(ele)
    del_loc(arr, n, ind+1)

x = eval(input("enter an array: "))
end = 1
while end != 0:
    n = 0
    for i in x:
        if type(i) == int:
            n += 1
        else:
            continue
    option = int(input('\n'"enter 1 for deleting at end"'\n'
                       "enter 2 for deleting at front"'\n'
                       "enter 3 for deleting at given position"'\n'
                       "enter 4 for deleting after a given value"'\n'
                       "enter 5 to quit the program"'\n'
                       ": "))
    if option == 1:
        del_end(x, n)
    elif option == 2:
        del_front(x, n)
    elif option == 3:
        location = int(input("enter location of deletion: "))
        del_loc(x, n, location)
    elif option == 4:
        ele = int(input("enter value after which you want to remove: "))
        del_after(x, n, ele)
    elif option == 5:
        print("program terminated, goodby-...")
        end = 0
