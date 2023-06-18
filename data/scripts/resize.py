#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力画像全てにリサイズ処理をする

from PIL import Image, ImageOps
import glob, os

IMG_WIDTH = 510
IMG_HEIGHT = 327
file_path = "./images/E/"
output_dir = "./images/out/E/"

for infile in glob.glob(file_path + "*.jpg"):
    file, _ = os.path.splitext(infile)
    with Image.open(infile) as im:
        im = im.resize(size=(IMG_WIDTH,IMG_HEIGHT),resample= Image.Resampling.BILINEAR)
        im.save(output_dir + os.path.basename(file) + "_resized.jpg")
