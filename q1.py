# Write a program to plot a bar chart in python to display the result of a school for five consecutive years

import matplotlib.pyplot as plt;import numpy as np
x = ["PHYSICS","MATHS","COMP.SC.","ENGLISH","CHEMISTRY"]
xpos = np.arange(len(x))
y1=[80,90,92,88,89]
y2 =[83,90,94,90,78]
y3 = [86,90,95,74,85]
y4 = [88,95,96,86,88]
y5 =  [90,99,91,84,80]
plt.xticks(xpos,x)
plt.bar(xpos-0.2,y1,width=0.1,label ='2004')
plt.bar(xpos-0.1,y2,width=0.1,label ='2005')
plt.bar(xpos,y3,width=0.1,label ='2006')
plt.bar(xpos+0.1,y4,width=0.1,label ='2007')
plt.bar(xpos+0.2,y5,width=0.1,label ='2008')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('RESULT')
plt.legend()
plt.show()