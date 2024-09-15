# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:11:11 2024

@author: Kim Quyên
"""

tong_chan = 0
tong_le = 0
for i in range(101):
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i
print("Tổng các số chẵn là:", tong_chan)
print("Tổng các số lẻ là:", tong_le)