# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:47:01 2024

@author: Kim Quyên
"""

so=float(input("Nhập số trong khoảng [-99; 99]: "))
while so <= -99 or so >= 99:
    so=float(input("Nhập lại số: "))
    print("Giá trị đã nhập là: ", so)