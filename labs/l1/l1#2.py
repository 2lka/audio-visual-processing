from PIL import Image
import numpy as np

image = Image.open('/home/dima/Desktop/Attachment.bmp')
pix = image.load()
size = image.size
lightness = np.zeros(size)

for i in range(size[0]):
    for j in range(size[1]):
        a, b, c = pix[i, j]
        pix[i, j] = 0, 0, c
        lightness[i, j] = (a + b + c) // 3
image.save('/home/dima/Desktop/bAttachment.bmp')
image.show()
print(lightness)

