#Emre Çamlıca, 150210071
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5,10,20)
y=[0.72, 1.63, 1.88, 3.39, 4.02, 3.89, 4.25, 3.99, 4.68, 5.03, 5.27, 4.82, 5.67, 5.95, 5.72, 6.01, 5.5, 6.41, 5.83, 6.33]

y1 = 0.5*x + 1.923
y2 = -0.0686*x**2 + 1.2203*x + 0.6030
y3 = 1.945*np.log(x) + 1.780

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y,'o', label='(x,y) pairs')
plt.plot(x,y1, 'b', label='y=0.5x+1.923')
plt.plot(x,y2, 'c', label='y=-0.0686x^2+1.2203x+0.6030')
plt.plot(x,y3, 'r', label='y=1.945ln(x)+1.780')

plt.legend(loc='upper left')
plt.show()
