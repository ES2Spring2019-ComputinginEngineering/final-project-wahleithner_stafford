# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:08:55 2019

@author: zosia
"""
#%matlibplot inline
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from IPython import get_ipython
ipython = get_ipython()

ipython.magic("matplotlib auto")
#change how plot appears
#saving graphs within the code
#generate videos from graph - rotation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[1,2,3,4,5,6,7,8,9,10]
y =[5,6,2,3,13,4,1,2,4,8]
z =[2,3,3,3,5,7,9,11,9,10]

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

for i in range(0, 360, 45):
    ax.view_init(None, i)
    plt.draw()
