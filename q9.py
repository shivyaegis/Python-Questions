# Write a program to calculate EMI for a loan using numpy.

import numpy as np
p = int(input("INPUT PRINCIPLE AMMOUNT ="))/1200
r = int(input("INPUT RATE OF INTEREST ="))
t = int(input("INPUT TIME ="))*12
emi = (p * r * np.power(1 + r, t)) / (np.power(1 + r, t) - 1)
print("Monthly EMI is= ", emi)