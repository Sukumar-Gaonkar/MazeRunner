import math
import os
from PIL import Image

dim = 24
k = 600/dim
print(k)
j = math.ceil(k)
size = j, j
filename = 'mario.gif'

file_parts = os.path.splitext(filename)
outfile = file_parts[0] + "_" + file_parts[1]

try:
    img = Image.open(filename)
    img = img.resize(size, Image.ANTIALIAS)
    img.save(outfile, "GIF")

except IOError as e:
    print(" An exception occured '%s'" % e)
