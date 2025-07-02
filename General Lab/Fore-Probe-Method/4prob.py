import matplotlib.pyplot as plt
import numpy as np

I = [ 1 ,    2 ,     3 ,   4 ,  5 ,   6 ,   7 ,  7.1 , 7.2 , 7.3 , 7.4 , 7.5,7.7 ,7.8]
V = [ 86.3 , 170 , 252 , 341 ,430 , 514 , 594 ,600,  608 ,  618,  626 , 630  ,650,660]

T = [34, 38 ,42, 46, 50, 54, 58, 62, 66,  70,  74,78, 82,  86, 90,  94,   98,  102, 106, 110, 114, 118  ,122, 126, 130, 134, 138, 142, 146, 150]
Vt= [261,249,238,230,221,208,193,179,164, 151, 136 ,118,107,96, 86.4,77.8, 70.6,63.8,58.2,53.8,48.4,44.1,40.2,36.3,33.2,29.6,26.5,23.6,21.6,19.0]
vv=[107,96, 86.4,77.8, 70.6,63.8,58.2,53.8,48.4,44.1,40.2,36.3,33.2,29.6,26.5,23.6,21.6,19.0]
tt=[82,  86, 90,  94,   98,  102, 106, 110, 114, 118  ,122, 126, 130, 134, 138, 142, 146, 150]
"""
plt.subplot(2,1,1)
plt.scatter(I,V)
plt.plot(I,V)
plt.subplot(2,1,2)
plt.scatter(tt,vv)
plt.grid(True)
plt.plot(tt,vv)
plt.show()
"""
fig = plt.figure()
gx = fig.add_subplot(211)
gx.plot(I,V)
gx.grid(True)
ax = fig.add_subplot(212)
ax.plot(T,Vt, 'ro-')
ax.margins(x=0, y=0)
grid_points = T
ygrid= Vt
ax.xaxis.set_ticks(grid_points)
ax.yaxis.set_ticks(ygrid)
ax.grid(True)
plt.show()
print(len(T))