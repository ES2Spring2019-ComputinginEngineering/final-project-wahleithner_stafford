#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 05:02:27 2019

@author: gillianwahleithner
"""

import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from IPython import get_ipython
ipython = get_ipython()
ipython.magic("matplotlib inline")

from Final_Project import readDataFile, normalize, userData, graphdata2D, graphdata3D, distancearray, knearestneighbor, topmaterials, returnmaterials

den, mod, stren, classif, prop_array = readDataFile("data.csv")
den, mod, stren, prop_array, d_min, d_max, m_min, m_max, s_min, s_max = normalize(den, mod, stren, prop_array)
test_case = userData(d_min, d_max, m_min, m_max, s_min, s_max)
graphdata2D(den, mod, stren, classif, test_case)    
graphdata3D(den, mod, stren, classif, test_case)
distance_array = distancearray(test_case[0,0], test_case[0,1], test_case[0,2], 
                               den, mod, stren)
finalclass = knearestneighbor(5, test_case[0,0], test_case[0,1], test_case[0,2], den, mod, stren, classif)
top_materials_array = topmaterials(finalclass, test_case[0,0], test_case[0,1], test_case[0,2], den, mod, stren, classif)
first_mat, second_mat, third_mat = returnmaterials(top_materials_array, finalclass)
