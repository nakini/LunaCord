"""
Here, we are going to read the coverage data.
"""

# Open the file.
fd = open("Copy of GSM900_Coverage by signal level.txt", 'r')
# fd = open("testGSM.txt", 'r')

# First, strip off the header. If possible extract the information from the header.
for i in range(1,12):
    print (fd.readline().strip())

# Now, read rest of the lines and convert them into floats and save the values in a 2D
# array.
array2D = []
for newLine in fd.readlines():
    # Read one line and strip of new line and split the string based on delimiter ";"
    tmp = newLine.strip()
    wordList = [x for x in tmp.split(";")]

    # Delete the 3rd column which is not going to use. 1st col = X, 2nd col = Y and 4th
    #  col = Gain in DB
    del wordList[2]

    # As the floating point is represented here by ',', replace it with a '.' and then
    # convert the string into a float.
    numList = [float(y.replace(',', '.')) for y in wordList]

    # Store for future use.
    array2D.append(numList)

# Close the file for good.
fd.close()

for i in range(334738, 334750):
    print array2D[i]
# print repr(array2D)

def getData():
    return array2D