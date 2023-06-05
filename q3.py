# Write a program in python to plot a pie chart on consumption of water in daily life.

import matplotlib.pyplot as plt
labels = 'DRINKING', 'TOILET', 'PERSONAL WASHING-BATH', 'PERSONAL WASHING-SHOWERS','CLOTHES WASHING' ,'WASHING UP' ,'OUTDORE','OTHERS'
sizes = [30, 21, 12, 13,8,7,5,4]
colors = ['PINK','BLUE','RED','LIGHTGREEN','PURPLE','GOLD', 'yellowgreen', 'lightcoral', 'MAGENTA']
explode = (0.1, 0.2, 0.5, 0.2, 0, 0.1, 0, 0.1)  # explode 1st slice
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140,explode=explode)
plt.show()