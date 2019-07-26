#/usr/bin/python

from PIL import Image
import numpy as np


icon = Image.open("mongo_leaf.bmp")


def scale_to_width(dimensions, width):
    height = (width * dimensions[1]) / dimensions[0]

    return (width, height)


def scale_by_multiple(dimensions, multiple):
    height = multiple * dimensions[1]
    width = multiple * dimensions[0]

    return (int(width), int(height))

scale_multiples = [0.25, 0.5, 0.75, 1.25, 1.5, 2, 2.5, 3]

for s in scale_multiples:
    filename = "scaled" + str(s) + ".bmp"
    icon.resize(scale_by_multiple(icon.size, s), Image.NEAREST).save(filename)
