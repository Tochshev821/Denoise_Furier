from scipy.integrate import dblquad
import math
from PIL import Image, ImageDraw

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
for i in range(len(f)): # count Fourier coeficents
    C = dblquad(lambda x, y: f[i] * math.sin(math.pi*x*n/width)*math.sin(math.pi*y*m/height)*math.sin(math.pi*k*x/width)*math.sin(math.pi*l*y/height), 0, width, lambda x: 0, lambda x: height)
print(f[j], C)# Сделать из С массив

#reconsruc the image
for n in range(width):
    for m in range(height):
        lambda x, y: C*math.sin(math.pi*n*x/width)*math.sin(math.pi*m*y/height)

