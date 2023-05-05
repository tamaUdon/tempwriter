#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import time
from escpos.printer import Usb

p = None

def init_printer():
    global p

    p = Usb(idVendor=0x04b8, idProduct=0x0202)
    # test print
    text = "Lorem ipsum dolor （中略） id est laborum."
    p.text(text)
    p.cut()

def output_and_cut(text):

    global p

    try:
        p.text(text)
        p.cut()
        time.sleep(1.0)
    except Exception as e:
        print(e)
