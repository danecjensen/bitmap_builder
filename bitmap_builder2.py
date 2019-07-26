#/usr/bin/python

from PIL import Image
import numpy as np


im = Image.open('template_bmp/argyle/dot_argyle_template.bmp')
im = im.convert('RGBA')

icon = Image.open("scaled1.25.bmp")
icon = icon.convert('RGBA')

print "\n"
print icon.getcolors()
print "\n"
print list(im.getdata())


def convert_color(c1, c2, data):
    # change color c1 to color c2
    (red, green, blue, alpha) = data[:, :, 0], data[
        :, :, 1], data[:, :, 2], data[:, :, 3]
    mask = (red == c1[0]) & (green == c1[1]) & (
        blue == c1[2]) & (alpha == c1[3])
    data[:, :, :4][mask] = [c2[0], c2[1], c2[2], c2[3]]
    return data


def get_mask(c1, data):
    (red, green, blue, alpha) = data[:, :, 0], data[
        :, :, 1], data[:, :, 2], data[:, :, 3]
    mask = (red == c1[0]) & (green == c1[1]) & (
        blue == c1[2]) & (alpha == c1[3])
    print mask
    # mask = Image.fromarray(mask)
    return mask

np_icon = np.array(icon)

alpha_icon = convert_color((0, 0, 0, 255), (0, 0, 0, 0), np_icon)
paste_icon = Image.fromarray(alpha_icon)
# mask = get_mask((0, 0, 0, 255), np_icon)
#  [(x1,y1), (x2,y2), ...]

# points_array = [(28, 25), (84, 25), (140, 25), (56, 106), (112, 106),
#                 (28, 187), (84, 187), (140, 187), (84, 349), (56, 268), (112, 268), (0, 106), (168, 106)]

points_array = [(42, 34), (126, 34), (42, 112), (42, 188), (126, 112), (126, 188), (0, 73), (84, 73), (168, 73),
                (0, 150), (84, 150), (168, 150), (84, 228), (84, 305), (84, 383), (42, 267), (126, 267), (42, 344), (126, 344)]

# print list(paste_icon.getdata())
dims = paste_icon.size
paste_point = (28 - int(dims[0] / 2), 25 - int(dims[1] / 2))

offset = (0, 1)

for pt in points_array:
    paste_point = (pt[0] + offset[0] - int(dims[0] / 2),
                   pt[1] + offset[1] - int(dims[1] / 2))
    im.paste(paste_icon, paste_point, paste_icon)


im.save("out.bmp")
