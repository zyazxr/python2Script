#!/usr/bin/env python
# encoding: utf-8

"""
@author: z00390414
@software: PyCharm
@file: tuxiangchuli.py
@time: 2018/1/27 20:38
"""
from __future__ import print_function
from PIL import ImageFilter
from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance

def func():
    pass


class Main(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    im = Image.open("IMG_20180127_200924.jpg").convert('L')
    print(im.format, im.size, im.mode)
    out = im.filter(ImageFilter.FIND_EDGES)
    imgEH = ImageEnhance.Contrast(out)
    # out.show()
    imgEH.enhance(3).show("30% more contrast")
    xsize, ysize = im.size

    # draw = ImageDraw.Draw(im)
    # draw.rectangle((0, 0, 200, 200), fill=(255, 0, 0, 128))
    # draw.rectangle((400, 400, 600, 600), fill=(255, 0, 0))
    print (xsize ,ysize)

    # try:
    #     with Image.open("IMG_20180127_200924.jpg") as im:
    #         print("IMG_20180127_200924.jpg", im.format, "%dx%d" % im.size, im.mode)
    # except IOError:
    #     pass

    # pass