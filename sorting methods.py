def bub_sort(list2):
    list1 = list2.copy()
    for i in range (0,len(list1)):
        for j in range (0,len(list1) - i - 1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j + 1] = list1[j+1],list1[j]
            else:
                continue
    print("array is sorted: ", str(list1))

def ins_sort(list2):
    list1 = list2.copy()
    n_ = len(list1)
    for i in range(1, n_):
        key = list1[i]
        j = i - 1
        while j >= 0 and key < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        else:
            list1[j + 1] = key
    print("array is sorted: ", str(list1))


def sel_sort(list2):
    list1 = list2.copy()
    n__ = len(list1)
    for i in range(0, n__):
        min_ = i
        for j in range(i+1, n__):
            if list1[j] < list1[min_]:
                min_ = j
        if list1[i] > list1[min_]:
            list1[i], list1[min_] = list1[min_], list1[i]
    print(list1)


print("WELCOME TO THE SORTED WORLD :D")
n = int(input("enter size of array"))
arr = []
print("enter elements")
for i in range(n):
    ele = int(input())
    arr.append(ele)
choice = 4
while choice != 3:
    print('\n'"now your array is set (back again) to: ", str(arr))
    choice = int(input("enter 0 for bubble sort"'\n'
                       "enter 1 for insertion sort"'\n'
                       "enter 2 for selection sort"'\n'
                       "enter 3 to quit the program"'\n'))
    if choice == 0:
        bub_sort(arr)
    elif choice == 1:
        ins_sort(arr)
    elif choice == 2:
        sel_sort(arr)
    elif choice == 3:
        print("program terminated... noooo please don't I -")
        break
    else:
        print("choose a valid option")