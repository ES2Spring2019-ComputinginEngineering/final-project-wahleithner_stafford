# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:08:55 2019

@author: zosia
"""
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math as m
from IPython import get_ipython
ipython = get_ipython()
ipython.magic("matplotlib inline")

#change how plot appears
#saving graphs within the code
#generate videos from graph - rotation

def readDataFile(filename):
    #function reads the data file, "data.csv" and reads three arrays of equal length:
    #density, modulus of elasticity, tensile strength
    csv_file = open(filename)
    total_row = sum(1 for row in csv_file)
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0     
    density = np.zeros(((total_row-1),))
    modulus = np.zeros(((total_row-1),))
    strength = np.zeros(((total_row-1),))
    classification = np.zeros(((total_row-1),))
    
    data_array = np.zeros((total_row-1, 4))

    index = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            density[index] = ((float(row[0])))
            modulus[index] = ((float(row[1])))
            strength[index] = ((float(row[2])))
            classification[index] = ((float(row[3])))
                
            data_array[index,0] = density[index]
            data_array[index,1] = modulus[index]
            data_array[index,2] = strength[index]
            data_array[index,3] = classification[index]
  
            index += 1
            line_count += 1
    csv_file.close()
    return density, modulus, strength, classification, data_array

def normalize(density, modulus, strength, data_array):
    d_min = min(density)
    d_max = max(density)
    m_min = min(modulus)
    m_max = max(modulus)
    s_min = min(strength)
    s_max = max(strength)
    for i in range(len(density)):
        density[i] = (density[i]-d_min)/(d_max - d_min)
        data_array[i, 0] = density[i]
    for index in range(len(modulus)):
        modulus[index] = (modulus[index]- m_min)/(m_max - m_min)
        data_array[index, 1] = modulus[index]
    for index in range(len(strength)):
        strength[index] = (strength[index]- s_min)/(s_max - s_min)
        data_array[index, 2] = strength[index]   
    return density, modulus, strength, data_array, d_min, d_max, m_min, m_max, s_min, s_max

def userData(d_min, d_max, m_min, m_max, s_min, s_max):
    density = input("What is the material's density? ")
    modulus = input("What is the material's modulus of elasticity? ")
    strength = input("What is the material's yield tensile strength? ")
    ndensity = (float(density) - d_min)/(d_max - d_min)
    nmodulus = (float(modulus) - m_min)/(m_max - m_min)
    nstrength = (float(strength) - s_min)/(s_max - s_min)
    test_array = np.zeros((1,3))
    test_array[0,0] = float(ndensity)
    test_array[0,1] = float(nmodulus)
    test_array[0,2] = float(nstrength)
    
    answer = input("Would you like the graphs to be interactive and appear in a different window? Yes/No: ")
    if (answer == "Yes") or (answer == "yes"):
        ipython.magic("matplotlib auto")
    return test_array

def graphdata2D(density, modulus, strength, classification,test_array):
    #density vs. tensile strength
    plt.figure()
    plt.plot(density[classification==0], strength[classification==0],"yo", label = "Magnesium")
    plt.plot(density[classification==1], strength[classification==1],"bo", label = "Aluminum")
    plt.plot(density[classification==2], strength[classification==2],"go", label = "Steel")
    plt.plot(density[classification==3], strength[classification==3],"ko", label = "Tungsten")
    plt.plot(density[classification==4], strength[classification==4],"co", label = "Zinc")
    plt.plot(density[classification==5], strength[classification==5],"mo", label = "Titanium")
    plt.plot(test_array[:,0],test_array[:,2], "ro", label = "Unknown")
    plt.title("Strength - Density")
    plt.xlabel("Density (g/cc)")
    plt.ylabel("Tensile Strength, at yield (MPa)")
    plt.legend()
    plt.grid()
    plt.savefig("density_strength.png")     #saves graph as a png file
    plt.show()
    
     #density vs. modulus of elasticity
    plt.figure()
    plt.plot(density[classification==0], modulus[classification==0],"yo", label = "Magnesium")
    plt.plot(density[classification==1], modulus[classification==1],"bo", label = "Aluminum")
    plt.plot(density[classification==2], modulus[classification==2],"go", label = "Steel")
    plt.plot(density[classification==3], modulus[classification==3],"ko", label = "Tungsten")
    plt.plot(density[classification==4], modulus[classification==4],"co", label = "Zinc")
    plt.plot(density[classification==5], modulus[classification==5],"mo", label = "Titanium")
    plt.plot(test_array[:,0],test_array[:,1], "ro", label = "Unknown")
    plt.title("Young's Modulus - Density")
    plt.xlabel("Density (g/cc)")
    plt.ylabel("Young's Modulus (GPa)")
    plt.legend()
    plt.grid()
    plt.savefig("density_modulus.png")
    plt.show()
    
    #modulus of elasticity vs. tensile strength
    plt.figure()
    plt.plot(modulus[classification==0], strength[classification==0], "yo", label = "Magnesium")
    plt.plot(modulus[classification==1], strength[classification==1], "bo", label = "Aluminum")
    plt.plot(modulus[classification==2], strength[classification==2], "go", label = "Steel")
    plt.plot(modulus[classification==3], strength[classification==3], "ko", label = "Tungsten")
    plt.plot(modulus[classification==4], strength[classification==4], "co", label = "Zinc")
    plt.plot(modulus[classification==5], strength[classification==5], "mo", label = "Titanium")
    plt.plot(test_array[:,1],test_array[:,2], "ro", label = "Unknown")
    plt.title("Young's Modulus - Strength")
    plt.xlabel("Young's Modulus (GPa)")
    plt.ylabel("Tensile Strength, at yield (MPa)")
    plt.legend()
    plt.grid()
    plt.savefig("modulus_strength.png", bbox_inches = "tight")
    plt.show()
    
def graphdata3D(density, modulus, strength, classification, test_array):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(density[classification == 0], modulus[classification == 0], strength[classification == 0], c='y', marker='o', label = "Magnesium")
    ax.scatter(density[classification == 1], modulus[classification == 1], strength[classification == 1], c='b', marker='o', label = "Aluminum")
    ax.scatter(density[classification == 2], modulus[classification == 2], strength[classification == 2], c='g', marker='o', label = "Steel")
    ax.scatter(density[classification == 3], modulus[classification == 3], strength[classification == 3], c='k', marker='o', label = "Tungsten")
    ax.scatter(density[classification == 4], modulus[classification == 4], strength[classification == 4], c='c', marker='o', label = "Zinc")
    ax.scatter(density[classification == 5], modulus[classification == 5], strength[classification == 5], c='m', marker='o', label = "Titanium")
    ax.scatter(test_array[:,0],test_array[:,1],test_array[:,2], c = 'r', marker = 'o')
    
    ax.set_xlabel("Density (g/cc)")
    ax.set_ylabel("Young's Modulus (GPa)")
    ax.set_zlabel("Tensile Strength, at yield (MPa)")
    plt.savefig("density_strength_modulus.png", bbox_inches = "tight")

#def distancearray(ndensity, nmodulus, nstrength, density, modulus, strength):
#    distance = np.zeros(len(density))
#    for i in range(len(density)):
#        distance[i] = m.sqrt((density[i]-ndensity)**2+(modulus[i]-nmodulus)**2 +(strength[i]-nstrength)**2)
#    print(distance)
#    return distance
#WHY WONT IT WORK??????? error says it got an array when it wanted a scalar -- but i want an array??
    
#def knearestneighbor:
    #from 3D arrays, create an array of the closest points and their classifications
    
#def topmaterials
    #find top three points with different classifications
    
#def denormalize
    #denormalize the data
    
#def returnmaterials
    #return classifications of top three closest points of different material
    #return a percentage correlating to how close the test case was to each
    #return denormalized data corresponding to these materials

#Call functions
den, mod, stren, classif, prop_array = readDataFile("data.csv")
den, mod, stren, prop_array, d_min, d_max, m_min, m_max, s_min, s_max = normalize(den, mod, stren, prop_array)
test_case = userData(d_min, d_max, m_min, m_max, s_min, s_max)
graphdata2D(den, mod, stren, classif, test_case)    
graphdata3D(den, mod, stren, classif, test_case)
distance_array = distancearray(test_case[:0], test_case[:1], test_case[:2], den, mod, stren)

#make driver