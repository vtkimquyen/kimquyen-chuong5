# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:51:47 2024

@author: Kim Quyên
"""
km=float(input("Số Km quãng đường đi được:"))
if km<=1:
 print("Số tiền là 15000d")
else:
    if 1<km<5:
     sotien = 15000 + (km - 1)*13500
    elif km>6:
     sotien = 15000 + (13500*4) + (11000*km)
    elif km>120:
     sotien *= 0.9
print("Số tiền phải trả là: ", sotien)
    