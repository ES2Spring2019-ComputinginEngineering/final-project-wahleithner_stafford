# Final Project: Material Identification

Our project focuses on classifying and identifying unknown materials. Most materials have some level of variance in their property measurements, so it is not always so simple to identify which material you have. Ensuring that this identification is correct can prevent future errors in process design and manufacturing. Our project is designed to identify and classify unknown materials. It will classify a material when provided information on the properties of a material. 

---------------------------------------------

## Instructions

- Open Final_Project.py and run the script (nothing will happen). 
- Open Final_Project_driver.py and run the script.
- Program will ask for the user's density, modulus of elasticity, and strength of their unknown material
- Enter one of the test cases given in the driver code
- Or, enter your own test case which must be within the range of the property (you can look at the min/max variables)
- The script will ask whether or not you want the graphs and tables to be interactive (which allows you to rotate the 3D graph)
- To be interactive, type 'yes', and to stay within the script, say 'no'
- If you say 'no' and then want to say 'yes', you must restart the kernel, but it is fine to say 'yes' and then 'no'
- The script will return the top three most likely materials, indicated with scores from 0 to 100, as well as a table of the average properties of each material

## File List

Final_Project.py:
- This is the main script of our code. 
- The script takes in input from the user and compares the user's test case to property data from six different materials.
- Using classification techniques, the program finds the top three closest materials to the test case.
- This script returns three 2-D graphs and one 3-D graph comparing the properties of all materials, the top three material names and their 'scores' indicating how close they are, and a table of the average property values for each material.

Final_Project_driver.py:
- This script calls the functions within the Final_Project.py script.
- It gives examples of test cases to use for each of the six materials, which should return a score of 100, as well as some random edge cases.

data.csv:
- This is a csv file that contains data of the three properties of each material, using different alloys.
- This data comes from MatWeb's Property Search.

README.md:
- This file gives a description of our program and how to run it.

density_modulus.png:
- This is the saved 2-D graph of density versus modulus for all materials, including the last used test case.

density_strength.png:
- This is the saved 2-D graph of density versus strength for all materials, including the last used test case.

modulus_strength.png:
- This is the saved 2-D graph of modulus versus strength for all materials, including the last used test case.

density_strength_modulus.png:
- This is the saved 3-D graph of all the properties for all materials, including the last used test case.

## Features
For this code, we used clustering techniques, classification, importing data from a file, and descriptive statistics. We included a few new modules in our program, including mpl_toolkits.myplot3d and IPython for 3D graphs and user interface. We used new functions within matplotlib module to create a table with colors and a 3D graph.

## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists
