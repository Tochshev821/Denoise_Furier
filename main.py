from scipy.integrate import dblquad
import math
from PIL import Image, ImageDraw
import numpy as np
import time
start_time = time.time()

# Read image
image = Image.open('screen_f.jpg')#'casino.jpg'
draw = ImageDraw.Draw(image)
width = image.size[0]# get width of image
height = image.size[1]# get height of image
pix = image.size[1]
pix = image.load()
x = [0]*width
y = [0]*height
# create list of coordinate of x and y
for i in range(width):
    x[i] = i
for i in range(height):
    y[i] = i

# у меня размер изображения width and height
f = [0]*width*height # наша функции заданная на всем промежутке
xx = 0 # count num of non zero pixels
for i in range(width):
    for j in range(height):
       r = pix[i, j][0] #узнаём значение красного цвета пикселя
       g = pix[i, j][1] #зелёного
       b = pix[i, j][2] #синего
       f[j] = r

       if f[j]>0:
           #print(f[y])
           xx = xx+1

       #print(pix[x,y])

print(f"координата х: {x[3]} координата у : {y[3]} значение функции : {f[3]}")

#print(len(f))
print(f"Размер изображения : {image.size}")
print(f"высота на ширину {width*height}")
print( f"количество ненулевых пикселей : {xx}")# количество ненулевых пикселей
C = [0]*width*height
for i in range(len(f)): # count Fourier coeficents
    C[i] = dblquad(lambda x, y: f[i] * math.sin(math.pi*x/width)*math.sin(math.pi*y/height)*math.sin(math.pi*x/width)*math.sin(math.pi*y/height), 0, height, lambda x: 0, lambda x: width)

print(f[2], C[2][0])# Сделать из С массив
non_zero_a = np.nonzero(C)
print(non_zero_a)
F = [0]*len(f)
   #reconsruct the image
for x in range(width):
    for y in range(height):
        F[x] = C[x][0]*math.sin(math.pi*x/width)*math.sin(math.pi*y/height) #lambda x, y: C[n]*math.sin(math.pi*x/width)*math.sin(math.pi*y/height)

non_zero_F = np.nonzero(F)
print(non_zero_F)

for x in range(width):
    for y in range(height):
       # r = pix[x, y][0] #узнаём значение красного цвета пикселя
       # g = pix[x, y][1] #зелёного
       # b = pix[x, y][2] #синего
       #
       draw.point((x, y), (int(F[x]), int(F[x]), int(F[x]))) #рисуем пиксель равный значению полуенной функции

image.save("result.jpg", "JPEG")

print("--- %s seconds ---" % (time.time() - start_time))

