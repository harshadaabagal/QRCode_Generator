# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 17:43:20 2022

@author: user
"""

import qrcode as qr #pip install qrcode

img =qr.make("https://www.google.com")

img.save("github.png")