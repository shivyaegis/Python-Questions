list1 = eval(input("enter elements of list 1"))
list2 = eval(input("enter elements of list 2"))
list3 = []
if len(list1) == len(list2):
    print('okay',end='')
    for i in range (0,len(list1)):
        val = list1[i] + list2[i]
        list3.append(val)
    print(list3)
else:
    print('no of elements not equal',end='')