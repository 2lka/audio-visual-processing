from PIL import Image


def resize_rows(image, new_size):
    new_image = Image.new('RGBA', (new_size, image.size[1]), (0, 0, 0, 0))
    pix = image.load()
    new_pix = new_image.load()
    for i in range(image.size[1]):
        counter = 0
        remainder = 1
        for j in range(image.size[0]):
            colour = pix[j, i]
            power = new_size / image.size[0]
            while power and counter < new_size:
                m = min(power, remainder)
                new_pix[counter, i] = tuple(int(colour[k] * m + new_pix[counter, i][k]) for k in range(4))
                power = power - m
                remainder = remainder - m
                if not remainder:
                    counter = counter + 1
                    remainder = 1
    return new_image


def resize_columns(image, new_size):
    new_image = Image.new('RGBA', (image.size[0], new_size), (0, 0, 0, 0))
    pix = image.load()
    new_pix = new_image.load()
    for i in range(image.size[0]):
        counter = 0
        remainder = 1
        for j in range(image.size[1]):
            colour = pix[i, j]
            power = new_size / image.size[1]
            while power and counter < new_size:
                m = min(power, remainder)
                new_pix[i, counter] = tuple(int(colour[k] * m + new_pix[i, counter][k]) for k in range(4))
                power = power - m
                remainder = remainder - m
                if not remainder:
                    counter = counter + 1
                    remainder = 1
    return new_image


def resize_image(image, new_size):
    return resize_rows(resize_columns(image, new_size[0]), new_size[1])


image = Image.open('/home/dima/PycharmProjects/audio-visual-processing/labs/l1/test.bmp')
image.show()
M, N = 3, 1/4

Ms = tuple(int(M * image.size[i]) for i in range(2))
Ks = tuple(int(N * Ms[i]) for i in range(2))

new_image = resize_image(resize_image(image, Ms), Ks)
new_image.show()

new_image = resize_image(image, Ks)
new_image.show()
