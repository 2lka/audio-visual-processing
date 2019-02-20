from PIL import Image


def myround(x):
    if x < 127:
        return 0
    else:
        return 255


image = Image.open('/home/dima/PycharmProjects/audio-visual-processing/labs/l2/image_changed.bmp')
size = image.size
new_image = Image.new('P', size, 0)

pix = image.load()
new_pix = new_image.load()
for i in range(1, size[0] - 1):
    for j in range(1, size[1] - 1):
        pixs = [pix[u, v] for u in range(i - 1, i + 2) for v in range(j - 1, j + 2)]
        m1 = (pixs[0] + pixs[1] + pixs[3] + pixs[4]) / 4
        m2 = (pixs[1] + pixs[2] + pixs[4] + pixs[5]) / 4
        m3 = (pixs[3] + pixs[4] + pixs[6] + pixs[7]) / 4
        m4 = (pixs[4] + pixs[5] + pixs[7] + pixs[8]) / 4
        d1 = ((pixs[0] - m1) ** 2 + (pixs[1] - m1) ** 2 + (pixs[3] - m1) ** 2 + (pixs[4] - m1) ** 2) / 4
        d2 = ((pixs[1] - m2) ** 2 + (pixs[2] - m2) ** 2 + (pixs[4] - m2) ** 2 + (pixs[5] - m2) ** 2) / 4
        d3 = ((pixs[3] - m3) ** 2 + (pixs[4] - m3) ** 2 + (pixs[6] - m3) ** 2 + (pixs[7] - m3) ** 2) / 4
        d4 = ((pixs[4] - m4) ** 2 + (pixs[5] - m4) ** 2 + (pixs[7] - m4) ** 2 + (pixs[8] - m4) ** 2) / 4
        m = min(d1, d2, d3, d4)
        if m == d1:
            new_pix[i, j] = myround(m1)
        elif m == d2:
            new_pix[i, j] = myround(m2)
        elif m == d3:
            new_pix[i, j] = myround(m3)
        elif m == d4:
            new_pix[i, j] = myround(m4)
new_image.show()

xor = Image.new('P', size, 255)
xor_pix = xor.load()
for i in range(1, size[0] - 1):
    for j in range(1, size[1] - 1):
        print(pix[i, j], new_pix[i, j])
        if pix[i, j] == new_pix[i, j]:
            xor_pix[i, j] = 255
        else:
            xor_pix[i, j] = 0
xor.show()

# convert работает не так, как надо
