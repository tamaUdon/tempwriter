#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import time
from escpos.printer import Usb

p = None

def init_printer():
    global p

    p = Usb(0x04b8, 0x0202, 0, profile="TM-T88III")
    # test print
    text = "初期化しました"
    p.text(text)
    p.cut()

def write(txt):
    global p
    try:
        p.text(txt)
    except Exception as e:
        print(e)

def image(path):
    global p
    try:
        p.image(path)
    except Exception as e:
        print(e)

def cut():
    global p
    try:
        p.cut()
    except Exception as e:
        print(e)
