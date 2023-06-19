list1 = [2,3,5,9,1,0]
n = len(list1)
for i in range(1,n):
    key = list1[i]
    j = i - 1
    while j>= 0 and key<list1[j]:
        list1[j+1]= list1[j]
        j-=1
    else:
        list1[j+1] = key
print(list1)
