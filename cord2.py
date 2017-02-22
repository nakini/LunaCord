"""
Given four vertices of a rectangle and the row and column count, we are going to find
out the coordinate of each row and column intersection.
"""
import math as mt
import numpy as np
from readCellData import getData
# Real coordinates of a rectangle.
minX, maxX, minY, maxY = 529.871, 531.186, 179.576, 180.571
stepSizeX = 1
stepSizeY = 1


# Dummy coordinates of a rectangle.
# minX,maxX,minY,maxY = 0.0, 2.0, 0.0, 2.0
# stepSizeX = 1
# stepSizeY = 1

# Setp size along the rectangle edges in X and Y direction
stepCountX = int(mt.ceil((maxX - minX)/stepSizeX))
stepCountY = int(mt.ceil((maxY - minY)/stepSizeY))

if __debug__:
    print ('Step size (X-dir): ' + repr(stepSizeX))
    print ('Step size (Y-dir): ' + repr(stepSizeY))
    print ('Cell count (X-dir): ' + repr(stepCountX))
    print ('Cell count (Y-dir): ' + repr(stepCountY))

# Now, generate the coordinates of each intersection either using a nested for-loop or
# using numpy in-built functions such as "linespace" and "meshgrid".

### Using nested-for loops.
vertices = []               # Container to hold all the X,Y coordinate tuples.
for iY in range(stepCountY+1):
    for jX in range(stepCountX+1):
        vertices.append([minX+stepSizeX*jX, minY+stepSizeY*iY])

if __debug__:
    print ("Total num of vertices: " + repr((stepCountX+1) * (stepCountY+1)))
    print ("Vertices: " + repr(vertices))

# ### Using numpy functions.
# # Get all the equally spaced points along X and Y direction of the rectangle.
# cordX = np.linspace(minX, maxX, stepCountX+1)
# cordY = np.linspace(minY, maxY, stepCountY+1)
#
# # Create a meshgrid which will have all the coordinates of intersection points.
# cordX_All, cordY_All = np.meshgrid(cordX, cordY)
#
# if __debug__:
#     print ("Total num of vertices: " + repr((stepCountX+1) * (stepCountY+1)))
#     print ("X coordinates: \n" + repr(cordX_All))
#     print ("Y coordinates: \n" + repr(cordY_All))

# Read the data from the text file
array2D = getData()
# Print few samples from the text file
for i in range(334738, 334750):
    print array2D[i]


# Filter data ...