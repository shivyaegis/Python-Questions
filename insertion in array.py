def check(arr_):
    global n
    for i in arr_:
        if i is None:
            continue
        else:
            n += 1


def insert_end(x, value, size, n):
    if n == size:
        print('\n'"array overflow, cannot be inserted")
    else:
        x[-1] = value
        print(x)


def insert_front(x, value, size, n):
    if n == size:
        print('\n'"array overflow, cannot be inserted")
    else:
        j = n
        while j >= 1:
            x[j] = x[j-1]
            j = j - 1
        if j == 0:
            x[j+1] = x[j]
        x[0] = value
        print(x)


def insert_pos(x, value, size, n, loc):
    if n == size:
        print('\n'"array overflow, cannot be inserted")
    elif loc > size:
        print('\n'"insertion not allowed here")
    else:
        if loc == 0:
            insert_front(x, value, size, n)
        elif loc == n:
            x[n] = value
            print(x)
        else:
            i = n
            while i > loc:
                x[i] = x[i-1]
                i = i - 1
            x[loc] = value
            print(x)


def insert_after(x, value, size, n, ele):
    if n == size:
        print('\n'"array overflow, cannot be inserted")
    if ele not in x:
        print("element not available")
    else:
        y = x.index(ele)
        for i in range(len(x)-1, y, -1):
            x[i] = x[i - 1]
            i = i - 1
        x[y] = value
        print(x)


print("WELCOME USER :D'\n")
a = int(input("enter size of your array: "))
arr = [None]*a
print('\n', arr)

while True:
    n = 0
    check(arr)
    option = int(input('\n'"type 1 for insertion at end"'\n'
                       "type 2 for insertion at beginning"'\n'
                       "type 3 for insertion at given position"'\n'
                       "type 4 for insertion after a given value"'\n'
                       "type 5 to quit"'\n'
                       ":"))
    if option == 1:
        val = int(input("enter value to insert at end: "))
        insert_end(arr, val, a, n)
    elif option == 2:
        val = int(input("enter value to insert at beginning: "))
        insert_front(arr, val, a, n)
    elif option == 3:
        val = int(input("enter value to insert at a position: "))
        location = int(input("enter location to insert element: "))
        insert_pos(arr, val, a, n, location)
    elif option == 4:
        val = int(input("enter value to insert: "))
        location = int(input("enter element after which you want to insert: "))
        insert_after(arr, val, a, n, location)
    elif option == 5:
        print("Program terminated. goodby-")
        break
