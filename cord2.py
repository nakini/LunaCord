"""
Given four vertices of a rectangle and the row and column count, we are going to find
out the coordinate of each row and column intersection.
"""
import math
import numpy as np

# Real coordinates of a rectangle.
minX, maxX, minY, maxY = 531.186, 529.871, 179.576, 180.571
stepCountX = 5
stepCountY = 5

# Dummy coordinates of a rectangle.
# minX,maxX,minY,maxY = 0.0, 2.0, 0.2, 2.2
# stepCountX = 2
# stepCountY = 2

# Setp size along the rectangle edges in X and Y direction
stepSizeX = (maxX - minX)/stepCountX
stepSizeY = (maxY - minY)/stepCountY

if __debug__:
    print ('Step size (X-dir): ' + repr(stepSizeX))
    print ('Step size (Y-dir): ' + repr(stepSizeY))

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

### Using numpy functions.
# Get all the equally spaced points along X and Y direction of the rectangle.
cordX = np.linspace(minX, maxX, stepCountX+1)
cordY = np.linspace(minY, maxY, stepCountY+1)

# Create a meshgrid which will have all the coordinates of intersection points.
cordX_All, cordY_All = np.meshgrid(cordX, cordY)

if __debug__:
    print ("Total num of vertices: " + repr((stepCountX+1) * (stepCountY+1)))
    print ("X coordinates: \n" + repr(cordX_All))
    print ("Y coordinates: \n" + repr(cordY_All))