import csv
import numpy as np
import matplotlib.pyplot as plt

def readDataFile(filename):
    #function reads the data file, "data.xlxs" and reads three arrays of equal length:
    #density, modulus of elasticity, tensile strength
    csv_file = open(filename)
    total_row = sum(1 for row in csv_file)

    print(total_row)
    

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
            print('Column names are '+ str(row))
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

def cluster_graph2D(density, modulus, strength, classification):
    #density vs. tensile strength
    plt.figure()
    plt.plot(density[classification==0], strength[classification==0],"r.", label = "Magnesium")
    plt.plot(density[classification==1], strength[classification==1],"b.", label = "Aluminum")
    plt.plot(density[classification==2], strength[classification==2],"g.", label = "Steel")
    plt.plot(density[classification==3], strength[classification==3],"k.", label = "Tungsten")
    plt.title("Strength - Density")
    plt.xlabel("Density")
    plt.ylabel("Tensile Strength (at yield)")
    plt.legend()
    plt.show()
    
    #density vs. modulus of elasticity
    plt.figure()
    plt.plot(density[classification==0], modulus[classification==0],"r.", label = "Magnesium")
    plt.plot(density[classification==1], modulus[classification==1],"b.", label = "Aluminum")
    plt.plot(density[classification==2], modulus[classification==2],"g.", label = "Steel")
    plt.plot(density[classification==3], modulus[classification==3],"k.", label = "Tungsten")
    plt.title("Modulus of Elasticity - Density")
    plt.xlabel("Density")
    plt.ylabel("Modulus of Elasticity")
    plt.legend()
    plt.show()
    
    #modulus of elasticity vs. tensile strength
    plt.figure()
    plt.plot(strength[classification==0], modulus[classification==0],"r.", label = "Magnesium")
    plt.plot(strength[classification==1], modulus[classification==1],"b.", label = "Aluminum")
    plt.plot(strength[classification==2], modulus[classification==2],"g.", label = "Steel")
    plt.plot(strength[classification==3], modulus[classification==3],"k.", label = "Tungsten")
    plt.title("Modulus of Elasticity - Strength")
    plt.xlabel("Tensile Strength (at yield)")
    plt.ylabel("Modulus of Elasticity")
    plt.legend()
    plt.show()
    
den, mod, stren, classif, prop = readDataFile("data.csv")
cluster_graph2D(den, mod, stren, classif)