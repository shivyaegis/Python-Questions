# Write a program in python to plot a graph for the function y = x^2

import matplotlib.pyplot as plt
import numpy as np
x = np.arange( -50 , 50)
y = x **2
plt.plot( x , y )
plt.show()