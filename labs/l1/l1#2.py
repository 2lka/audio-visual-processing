from PIL import Image

image = Image.open('triangle.bmp')
pix = image.load()
size = image.size
for i in range(size.width):
    for j in range(size.height):
        r, g, b, a = pix[i, j]
        lightness = (r + g + b) // 3
        pix[i, j] = lightness, lightness, lightness, 255
image.save('new_triangle.bmp')
image.show()
print(pix)
