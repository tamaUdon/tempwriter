#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力画像全てに左右反転処理をする

from PIL import Image, ImageOps
import glob, os

file_path = "./images/out/E/"
output_dir = "./images/out/E/"

for infile in glob.glob(file_path + "*.jpg"):
    file, _ = os.path.splitext(infile)
    with Image.open(infile) as im:
        im = im_flipped = ImageOps.mirror(im)
        # im = im.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        im.save(output_dir + os.path.basename(file) + "_flipped.jpg")
