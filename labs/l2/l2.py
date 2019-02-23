from PIL import Image
from functools import reduce


def myround(x):
    if x < 127:
        return 0
    else:
        return 255


image = Image.open('/home/dima/PycharmProjects/audio-visual-processing/labs/l2/image_changed.bmp')
size = image.size
new_image = Image.new(image.mode, size, 0)

pix = image.load()
new_pix = new_image.load()
for i in range(1, size[0] - 1):
    for j in range(1, size[1] - 1):
        ms = [[reduce(lambda x, y: x + y, [pix[i + x + u, j + y + v] / 4 for x in range(-1, 1) for y in range(-1, 1)]) for v in range(2)] for u in range(2)]
        ds = [[reduce(lambda x, y: x + y, [((pix[i + x + u, j + y + v] - ms[u][v]) ** 2) / 4 for x in range(-1, 1) for y in range(-1, 1)]) for v in range(2)] for u in range(2)]
        u, v = 0, 0
        for x in range(2):
            for y in range(2):
                if ds[x][y] < ds[u][v]:  # если изменить знак, то выделяются границы изображения
                    u, v = x, y
        new_pix[i, j] = myround(ms[u][v])
new_image.show()

xor = Image.new(image.mode, size, 255)
xor_pix = xor.load()
for i in range(1, size[0] - 1):
    for j in range(1, size[1] - 1):
        if pix[i, j] == new_pix[i, j]:
            xor_pix[i, j] = 255
        else:
            xor_pix[i, j] = 0
xor.show()

# convert работает не так, как надо
