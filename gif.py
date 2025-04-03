import imageio.v3 as im

im_names = ['m1.png', 'm2.png','m3.png', 'm4.png']
images = []

for im_name in im_names:
    images.append(im.imread(im_name))

im.imwrite('messi.gif', images, duration = 500, loop = 0)