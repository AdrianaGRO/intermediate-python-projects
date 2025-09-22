import numpy as np
from PIL import Image



#Create a 3D array (height, width, color channels)

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)


#Make a red pixel at row 1, column 3
data[1:4, 1:3] = [255, 0, 0]
data[1:4, 1:3] = [255, 200, 150]
data[1:4, 1:3] = [155, 205, 255]

#Convert the array to an image
img = Image.fromarray(data, 'RGB')
# Save with relative path to current file
img.save('/Users/adricati/Personal Development/intermediate-python-projects/17_ OOP_Object_Oriented_Programming/06_math_painter/canvas.png')