#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 05:02:27 2019

@author: gillianwahleithner
"""

from Final_Project import readDataFile, normalize, userData, graphdata2D, graphdata3D, distancearray, knearestneighbor, topmaterials, returnmaterials, returnproperty, denormalize

den, mod, stren, classif, prop_array = readDataFile("data.csv")
den, mod, stren, prop_array, d_min, d_max, m_min, m_max, s_min, s_max = normalize(den, mod, stren, prop_array)
test_case = userData(d_min, d_max, m_min, m_max, s_min, s_max)
graphdata2D(den, mod, stren, classif, test_case)    
graphdata3D(den, mod, stren, classif, test_case)
distance_array = distancearray(test_case[0,0], test_case[0,1], test_case[0,2], den, mod, stren)
finalclass = knearestneighbor(5, test_case[0,0], test_case[0,1], test_case[0,2], den, mod, stren, classif)
top_materials_array, top_dist_array = topmaterials(finalclass, test_case[0,0], test_case[0,1], test_case[0,2], den, mod, stren, classif)
first_mat, second_mat, third_mat = returnmaterials(top_materials_array, finalclass, top_dist_array)
den, mod, stren, prop_array = denormalize(den, mod, stren, prop_array, d_min, d_max, m_min, m_max, s_min, s_max)
returnproperty(den, mod, stren, classif)

#Test Cases:

#cases with high scores:
#45, 1.78, 138 = Magnesium
#69, 2.7, 145 = Aluminum
#200, 7.87, 676 = Steel
#365, 18.5, 586 = Tungsten
#85.5, 6.3, 290 = Zinc
#102, 4.65, 940 = Titanium

#Edge Cases:
#150, 5, 200 = Zinc
#300, 5, 200 = Steel
#50, 5, 800 = Titanium

#Based on property table given, feel free to test other values.