Dict1 = eval(input("Enter key value pairs"))
list1 = []
for i in Dict1:
    list1.append(i)
j = 1
k = 0
while k != len(list1)-1:
    for i in range(0,len(list1)-j):
        if list1[i] > list1[i+1]:
            list1[i] ,list1[i+1] = list1[i+1], list1[i]
            list1[i+1] = list1[i]
    j += 1
    k += 1
print(list1)
