# Write a program for linear search
import numpy as np

def ls(a,b,c):
    if b>=len(a):
        return -1
    if a[b]==c:
        return b+1
    return ls(a,b+1,c)

a = np.arange(1,11,1)
print("LIST - ",a)
c = int(input("INPUT A ELEMENT TO SEARCH - "))
print("INDEX OF THE ELEMENT",c,"IS -",ls(a,0,c)-1)