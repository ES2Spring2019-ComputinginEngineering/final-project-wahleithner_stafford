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
#user interface,soecial print functions
#labels for 3D
#animation
#driver


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

def graphdata2D(density, modulus, strength, classification, test_array):
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
    plt.title("Modulus of Elasticity - Density")
    plt.xlabel("Density (g/cc)")
    plt.ylabel("Modulus of Elasticity (GPa)")
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
    plt.title("Modulus of Elasticity - Strength")
    plt.xlabel("Modulus of Elasticity (GPa)")
    plt.ylabel("Tensile Strength, at yield (MPa)")
    plt.legend()
    plt.grid()
    plt.savefig("modulus_strength.png", bbox_inches = "tight")
    plt.show()
    
def graphdata3D(density, modulus, strength, classification, test_array):
    fig = plt.figure()
    ax = Axes3D(fig)
    
    ax.scatter(density[classification == 0], modulus[classification == 0], strength[classification == 0], c='y', marker='o', label = "Magnesium")
    ax.scatter(density[classification == 1], modulus[classification == 1], strength[classification == 1], c='b', marker='o', label = "Aluminum")
    ax.scatter(density[classification == 2], modulus[classification == 2], strength[classification == 2], c='g', marker='o', label = "Steel")
    ax.scatter(density[classification == 3], modulus[classification == 3], strength[classification == 3], c='k', marker='o', label = "Tungsten")
    ax.scatter(density[classification == 4], modulus[classification == 4], strength[classification == 4], c='c', marker='o', label = "Zinc")
    ax.scatter(density[classification == 5], modulus[classification == 5], strength[classification == 5], c='m', marker='o', label = "Titanium")
    ax.scatter(test_array[:,0],test_array[:,1],test_array[:,2], c = 'r', marker = 'o')
    
    ax.set_xlabel("Density (g/cc)")
    ax.set_ylabel("Modulus of Elasticity (GPa)")
    ax.set_zlabel("Tensile Strength, at yield (MPa)")
    plt.title("Density - Modulus - Strength")
    plt.savefig("density_strength_modulus.png", bbox_inches = "tight")
    plt.show()

def distancearray(ndensity, nmodulus, nstrength, density, modulus, strength):
    distance = np.zeros(len(density))
    for i in range(len(density)):
        distance[i] = m.sqrt((density[i]-ndensity)**2+(modulus[i]-nmodulus)**2 +(strength[i]-nstrength)**2)
    return distance
    
def knearestneighbor(k, ndensity, nmodulus, nstrength, density, modulus, strength, classification):
    distance = distancearray(ndensity, nmodulus,nstrength, density, modulus, strength)
    k_array = distance.argsort()[:k]
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    for i in k_array:
        if classification[i] == 0:
            count_0 += 1
        elif classification[i] == 1:
            count_1 += 1
        elif classification[i] == 2:
            count_2 += 2
        elif classification[i] == 3:
            count_3 += 3
        elif classification[i] == 4:
            count_4 += 4
        else:
            count_5 += 5
    if (count_0 > count_1) and (count_0 > count_2) and (count_0 > count_3) and (count_0 > count_4) and (count_0 > count_5):
        finalclassification = 0
    elif (count_1 > count_0) and (count_1 > count_2) and (count_1 > count_3) and (count_1 > count_4) and (count_1 > count_5):
        finalclassification = 1
    elif (count_2 > count_0) and (count_2 > count_1) and (count_2 > count_3) and (count_2 > count_4) and (count_2 > count_5):
        finalclassification = 2
    elif (count_3 > count_0) and (count_3 > count_1) and (count_3 > count_2) and (count_3 > count_4) and (count_3 > count_5):
        finalclassification = 3
    elif (count_4 > count_0) and (count_4 > count_1) and (count_4 > count_2) and (count_4 > count_3) and (count_4 > count_5):
        finalclassification = 4
    elif (count_5 > count_0) and (count_5 > count_1) and (count_5 > count_2) and (count_5 > count_3) and (count_5 > count_4):
        finalclassification = 5
    return finalclassification


def topmaterials(finalclassification, ndensity, nmodulus, nstrength, density, modulus, strength, classification):
    distance = distancearray(ndensity, nmodulus,nstrength, density, modulus, strength)
    t_array = distance.argsort()[:]
    top_distance_array = np.zeros(3)
    top_array = np.zeros(3)
    top_array[0] = finalclassification
    top_distance_array[0] = min(distance)
    p = 1
    for x in range(len(t_array)-1):
        for i in t_array:
            if classification[i] != classification[i+1] and (classification[i] != top_array[p]) and (classification[i] != top_array[p-1]) and (classification[i] != finalclassification):
                top_array[p] = classification[i]
                top_distance_array[p] = distance[i]
                if p < 2:
                    p += 1
                else:
                    break
    return top_array, top_distance_array
    
def returnmaterials(top_array, final_classification, top_distance_array):
    #return classification of material and three most likely materials
    #first material classification
    if final_classification == 0:
        first_material = "Magnesium"
    elif final_classification == 1:
        first_material = "Aluminum"
    elif final_classification == 2:
        first_material = "Steel"
    elif final_classification == 3:
        first_material = "Tungsten"
    elif final_classification == 4:
        first_material = "Zinc"
    elif final_classification == 5:
        first_material = "Titanium"
        
    #second material classification     
    if top_array[1] == 0:
        second_material = "Magnesium"
    elif top_array[1] == 1:
        second_material = "Aluminum"
    elif top_array[1] == 2:
        second_material = "Steel"
    elif top_array[1] == 3:
        second_material = "Tungsten"
    elif top_array[1] == 4:
        second_material = "Zinc"
    elif top_array[1] == 5:
        second_material = "Titanium"
    
    #third material classification    
    if top_array[2] == 0:
        third_material = "Magnesium"
    elif top_array[2] == 1:
        third_material = "Aluminum"
    elif top_array[2] == 2:
        third_material = "Steel"
    elif top_array[2] == 3:
        third_material = "Tungsten"
    elif top_array[2] == 4:
        third_material = "Zinc"
    elif top_array[2] == 5:
        third_material = "Titanium"
    
    percentage_array = np.zeros(3)
    for i in range(len(top_distance_array)):
        percentage_array[i] = 1 - top_distance_array[i]
    
    print("\nThe first choice in material is ", first_material)
    print("Likelihood of this material: ", round((percentage_array[0])*100, 3), "%")
    print("\nThe second choice in material is ", second_material)
    print("Likelihood of this material: ", round((percentage_array[1])*100, 3), "%") 
    print("\nThe third choice in material is ", third_material)
    print("Likelihood of this material: ", round((percentage_array[2])*100, 3), "%")
    
    return first_material, second_material, third_material
    
def denormalize(density, modulus, strength, data_array, d_min, d_max, m_min, m_max, s_min, s_max):
    for i in range(len(density)):
        density[i] = (density[i]+d_min)*(d_max - d_min)
        data_array[i, 0] = density[i]
    for index in range(len(modulus)):
        modulus[index] = (modulus[index]+ m_min)*(m_max - m_min)
        data_array[index, 1] = modulus[index]
    for index in range(len(strength)):
        strength[index] = (strength[index]+ s_min)*(s_max - s_min)
        data_array[index, 2] = strength[index] 
    return density, modulus, strength, data_array

def returnproperty(density, modulus, strength, classification):
    magnesium = np.zeros(3)
    aluminum = np.zeros(3)
    steel = np.zeros(3)
    tungsten = np.zeros(3)
    zinc = np.zeros(3)
    titanium = np.zeros(3)
    
    magnesium[0] = round(sum(density[classification == 0])/len(density[classification ==0]), 3)
    magnesium[1] = round(sum(modulus[classification == 0])/len(modulus[classification ==0]), 3)
    magnesium[2] = round(sum(strength[classification == 0])/len(strength[classification ==0]), 3)
    aluminum[0] = round(sum(density[classification == 1])/len(density[classification ==1]), 3)
    aluminum[1] = round(sum(modulus[classification == 1])/len(modulus[classification ==1]), 3)
    aluminum[2] = round(sum(strength[classification == 1])/len(strength[classification ==1]), 3)
    steel[0] = round(sum(density[classification == 2])/len(density[classification ==2]), 3)
    steel[1] = round(sum(modulus[classification == 2])/len(modulus[classification ==2]), 3)
    steel[2] = round(sum(strength[classification == 2])/len(strength[classification ==2]), 3)
    tungsten[0] = round(sum(density[classification == 3])/len(density[classification ==3]), 3)
    tungsten[1] = round(sum(modulus[classification == 3])/len(modulus[classification ==3]), 3)
    tungsten[2] = round(sum(strength[classification == 2])/len(strength[classification ==3]), 3)
    zinc[0] = round(sum(density[classification == 4])/len(density[classification ==4]), 3)
    zinc[1] = round(sum(modulus[classification == 4])/len(modulus[classification ==4]), 3)
    zinc[2] = round(sum(strength[classification == 4])/len(strength[classification ==4]), 3)
    titanium[0] = round(sum(density[classification == 5])/len(density[classification ==5]), 3)
    titanium[1] = round(sum(modulus[classification == 5])/len(modulus[classification ==5]), 3)
    titanium[2] = round(sum(strength[classification == 5])/len(strength[classification ==5]), 3)
    

    data = [magnesium, aluminum, steel, tungsten, zinc, titanium]
    
    columns = ("Density (g/cc)", "Modulus of Elasticty (GPa)", "Tensile Strength (MPa)")
    rows = ["Magnesium", "Aluminum", "Steel", "Tungsten", "Zinc", "Titanium"]
    
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
 
    fig, axs =plt.subplots(figsize = (8,2.3))
    axs.axis('off')
    axs.table(cellText= data,rowLabels=rows, rowColours=colors, colLabels=columns, loc='center')
    plt.title("Properties of All Materials")
    plt.show()

    

#Call functions
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