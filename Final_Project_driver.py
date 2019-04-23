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

from Final_Project import readDataFile, normalize, userData, graphdata2D, 
graphdata3D

den, mod, stren, classif, prop_array = readDataFile("data.csv")
den, mod, stre, prop_array = normalize(den, mod, stren, prop_array)
test_case = userData()
graphdata2D(den, mod, stren, classif, test_case)    
graphdata3D(den, mod, stren, classif, test_case)

