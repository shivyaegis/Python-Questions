while True:
    arr = eval(input("enter elements of array"))
    obj = int(input("enter element to search for in array: "))
    count = 0
    for i in range(0,len(arr)):
        if arr[i] == obj:
            print("element", str(obj), "found at ", str(i))
            count += 1
        else:
            continue
    if count == 0:
        print("element not found :((")
    else:
        print("no of times element was found is: ", str(count))
    choose = int(input("write any number to run again and 1 to quit: "))
    if choose == 1:
        print("program terminated.")
        break
    else:
        print('\n'"welcome back :) ")
        continue
