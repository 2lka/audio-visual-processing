from PIL import Image
import numpy as np

image = Image.open('/home/dima/PycharmProjects/audio-visual-processing/labs/l1/triangle.bmp')
pix = image.load()
size = image.size
lightness = np.zeros(size)
for i in range(size[0]):
    for j in range(size[1]):
        r, g, b, a = pix[i, j] #используется RGBA
        lightness[i, j] = (r + g + b) // 3
        pix[i, j] = int(lightness[i, j]), int(lightness[i, j]), int(lightness[i, j])
image.save('/home/dima/PycharmProjects/audio-visual-processing/labs/l1/new_triangle.bmp')
image.show()
print(lightness)
