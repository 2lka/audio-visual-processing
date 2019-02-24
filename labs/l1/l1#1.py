from PIL import Image


def resize_rows(image, new_width):
    new_image = Image.new(image.mode, (new_width, image.height))
    pix = image.load()
    new_pix = new_image.load()
    for i in range(image.height):
        j, k = 0, 0
        jpower, kpower = new_width, image.width
        while j < image.width and k < new_width:
            mpower = min(jpower, kpower)
            jpower -= mpower
            kpower -= mpower
            new_pix[k, i] = tuple(new_pix[k, i][l] + (mpower * pix[j, i][l]) // image.width for l in range(len(pix[j, i])))
            if jpower == 0:
                j += 1
                jpower = new_width
            if kpower == 0:
                k += 1
                kpower = image.width
    return new_image


def resize_columns(image, new_height):
    new_image = Image.new(image.mode, (image.width, new_height))
    pix = image.load()
    new_pix = new_image.load()
    for i in range(image.width):
        j, k = 0, 0
        jpower, kpower = new_height, image.height
        while j < image.height and k < new_height:
            mpower = min(jpower, kpower)
            jpower -= mpower
            kpower -= mpower
            new_pix[i, k] = tuple(new_pix[i, k][l] + (mpower * pix[i, j][l]) // image.height for l in range(len(pix[i, j])))
            if jpower == 0:
                j += 1
                jpower = new_height
            if kpower == 0:
                k += 1
                kpower = image.height
    return new_image


def resize_image(image, new_size):
    return resize_rows(resize_columns(image, new_size[1]), new_size[0])


image = Image.open('test.bmp')  # image.bmp
image.show()

M, N = 4, 1/3
Ms = tuple(int(M * image.size[i]) for i in range(2))
Ks = tuple(int(N * Ms[i]) for i in range(2))

new_image = resize_image(resize_image(image, Ms), Ks)
new_image.show()

new_image = resize_image(image, Ks)
new_image.show()
