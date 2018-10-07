import math
import os
from PIL import Image

dim = 50
k = 600/dim
print(k)
j = math.ceil(k)
size = j, j
filename1 = 'mario.gif'
filename2 = 'wall.gif'

file_parts1 = os.path.splitext(filename1)
file_parts2 = os.path.splitext(filename2)
outfile1 = file_parts1[0] + "_" + file_parts1[1]
outfile2 = file_parts2[0] + "_" + file_parts2[1]

try:
    img = Image.open(filename1)
    img = img.resize(size, Image.ANTIALIAS)
    img.save(outfile1, "GIF")

    img = Image.open(filename2)
    img = img.resize(size, Image.ANTIALIAS)
    img.save(outfile2, "GIF")

except IOError as e:
    print(" An exception occured '%s'" % e)
