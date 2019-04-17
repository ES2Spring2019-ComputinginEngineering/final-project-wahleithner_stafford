# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:08:55 2019

@author: zosia
"""
#%matlibplot inline
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from IPython import get_ipython
ipython = get_ipython()

ipython.magic("matplotlib auto")
#change how plot appears
#saving graphs within the code
#generate videos from graph - rotation

def graphdata(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    den = prop[:, 0]
    mod = prop[:, 1]
    stren = prop[:, 2]
    classif = prop[:, 3]
    
    ax.scatter(x, y, z, c='r', marker='o')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

prop = np.array([[1,2,3,4,5,6,7,8,9,10], [5,6,2,3,13,4,1,2,4,8], [2,3,3,3,5,7,9,11,9,10]])