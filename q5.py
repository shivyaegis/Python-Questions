# Write a program for bubble sort.

a = [10,21,22,2,3,0,21.3,31]
print("ORIGINAL LIST = "+str(a))
for i in range (1,len(a)):
    k = a[i]
    j = i - 1
    while j >= 0 and k < a[j]:
        a[j+1]=a[j]
        j-=1
    else :
        a[j+1]=k
print("SORTED LIST = "+str(a))