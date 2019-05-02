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
#interactive python, allows graphs to be interactive or not:
ipython = get_ipython()
ipython.magic("matplotlib inline")
#To do:
#user interface,special print functions
#animation


def readDataFile(filename):
    #This function reads the data file, "data.csv" and creates four arrays of equal length:
    #density, modulus of elasticity, tensile strength, and classification
    #It then adds these arrays to a 4D array that contains all of our data
   
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
    #This function normalizes our data in all the arrays
    #It returns the min/max of each property so we can denormalize it at the end,
    #as well as normalize our user input
   
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
    #This function takes in user input for the properties of an unknown material,
    #and then normalizes it
    #It also asks the user whether or not the graphs should be interactive
    #If you first say 'no', and then want to say 'yes', you must restart the kernel
    
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
    #This function creates three 2D graphs comparing all of the properties
    #of the materials and the unknown point
    #It also saves the graphs as images in our GitHub file
    
    #Density vs. tensile strength
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
    
    #Density vs. modulus of elasticity
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
    
    #Modulus of elasticity vs. tensile strength
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
    #This function creates a 3D graph of all of our properties
    #If the user chooses to make it interactive, the graph can be manipulated
    
    fig = plt.figure()
    ax = Axes3D(fig)
    
    ax.scatter(density[classification == 0], modulus[classification == 0], strength[classification == 0], c='y', marker='o', label = "Magnesium")
    ax.scatter(density[classification == 1], modulus[classification == 1], strength[classification == 1], c='b', marker='o', label = "Aluminum")
    ax.scatter(density[classification == 2], modulus[classification == 2], strength[classification == 2], c='g', marker='o', label = "Steel")
    ax.scatter(density[classification == 3], modulus[classification == 3], strength[classification == 3], c='k', marker='o', label = "Tungsten")
    ax.scatter(density[classification == 4], modulus[classification == 4], strength[classification == 4], c='c', marker='o', label = "Zinc")
    ax.scatter(density[classification == 5], modulus[classification == 5], strength[classification == 5], c='m', marker='o', label = "Titanium")
    ax.scatter(test_array[:,0],test_array[:,1],test_array[:,2], c = 'r', marker = 'o', label = "Unknown")
    
    ax.set_xlabel("Density (g/cc)")
    ax.set_ylabel("Modulus of Elasticity (GPa)")
    ax.set_zlabel("Tensile Strength, at yield (MPa)")
    plt.title("Density - Modulus - Strength")
    plt.legend()
    plt.savefig("density_strength_modulus.png", bbox_inches = "tight")
    plt.show()

def distancearray(ndensity, nmodulus, nstrength, density, modulus, strength):
    #This function creates an array, distance, with the distances
    # of every point from the test case
    
    distance = np.zeros(len(density))
    for i in range(len(density)):
        distance[i] = m.sqrt((density[i]-ndensity)**2+(modulus[i]-nmodulus)**2 +(strength[i]-nstrength)**2)
    return distance
    
def knearestneighbor(k, ndensity, nmodulus, nstrength, density, modulus, strength, classification):
    #This function performs k nearest neighbor.
    #It creates an array, k_array, from the distance array
    #k_array has 'k' indices of the distance array sorted min to max
    #It then finds what the classification is for each point in k_array
    #Whichever classification has the majority of the 'k' points,
    #is the final classification of the unknown material
    
    distance = distancearray(ndensity, nmodulus,nstrength, density, modulus, strength)
    k_array = distance.argsort()[:k] #array of indices of smallest k distances
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
    #This function finds the indices of the top 3 materials
    #that the test case is closest to, with the k nearest being first
    #t_array has the indices of the distant array sorted min to max
    #The code goes through t_array and finds points whose classifications
    #are different then all the ones before it, and puts the 
    #classifications into top_array, and their correspoding distances
    #into top_distance_array - this gives us the top 3 materials
    
    distance = distancearray(ndensity, nmodulus,nstrength, density, modulus, strength)
    t_array = distance.argsort()[:]  #array of indices of the sorted distance
    top_distance_array = np.zeros(3) #array of distances corresponding to the 3 min distances in t_array
    top_array = np.zeros(3) #array of classifications of the smallest distances
    top_array[0] = finalclassification
    top_distance_array[0] = min(distance)
    p = 1
    for x in range(len(t_array)-1):
        for i in t_array[0:146]:
            if classification[i] != classification[i+1] and (classification[i] != top_array[p]) and (classification[i] != top_array[p-1]) and (classification[i] != finalclassification):
                top_array[p] = classification[i]
                top_distance_array[p] = distance[i]
                if p < 2:
                    p += 1
                else:
                    break
    return top_array, top_distance_array
    
def returnmaterials(top_array, final_classification, top_distance_array):
    #This function assigns each classification to a material and
    #returns which material name each of the most likely materials is
    #It also gives each material a 'score' based on how close
    #it's distance is to our test case compared to the others

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
    
    score_array = np.zeros(3)
    top_distances_sum = np.sum(top_distance_array)
    
    for i in range(len(top_distance_array)):
        score_array[i] = 1 - (top_distance_array[i])/top_distances_sum
    
    print("\nThe first choice in material is ", first_material)
    print("Score of this material: ", round((score_array[0])*100, 2))
    print("\nThe second choice in material is ", second_material)
    print("Score of this material: ", round((score_array[1])*100, 2)) 
    print("\nThe third choice in material is ", third_material)
    print("Score of this material: ", round((score_array[2])*100, 2))
    print("Scores are given with 100 being the best choice")
    
    return first_material, second_material, third_material
    
def denormalize(density, modulus, strength, data_array, d_min, d_max, m_min, m_max, s_min, s_max):
    #This function denormalizes all of the data so that we can
    #return it as a table to the user
    
    for i in range(len(density)):
        density[i] = ((density[i])*(d_max - d_min)) + d_min
        data_array[i, 0] = density[i]
    for index in range(len(modulus)):
        modulus[index] = ((modulus[index])*(m_max - m_min)) + m_min
        data_array[index, 1] = modulus[index]
    for index in range(len(strength)):
        strength[index] = ((strength[index])*(s_max - s_min)) + s_min
        data_array[index, 2] = strength[index] 
    return density, modulus, strength, data_array

def returnproperty(density, modulus, strength, classification):
    #This function returns a table with the average of all
    #property values of each material
    
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
    
