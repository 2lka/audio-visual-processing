from PIL import Image

image = Image.open('/home/dima/PycharmProjects/audio-visual-processing/labs/l1/triangle.bmp')
pix = image.load()
size = image.size
for i in range(size.width):
    for j in range(size.height):
        r, g, b, a = pix[i, j]
        lightness = (r + g + b) // 3
        pix[i, j] = lightness, lightness, lightness, 255
image.save('/home/dima/PycharmProjects/audio-visual-processing/labs/l1/new_triangle.bmp')
image.show()
print(pix)
