from PIL import Image

image = Image.open('/home/dima/Desktop/Attachment.bmp')
image2 = image.copy()
size = image.size
M, N = 20, 1/30
K = M*N

new_size = size
for i in [M, N]:
    new_size = [j*i for j in new_size]
    image.thumbnail(new_size)
image.show()

new_size2 = [i*K for i in size]
image2.thumbnail(new_size2)
image2.show()