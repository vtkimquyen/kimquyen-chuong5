# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:56:54 2024

@author: Kim Quyên
"""

n=int(input("Nhập số và tính (2+4+6+..+n):"))
tinh=0
for i in range(2, n+1, 2):
    tinh += i
print("Kết quả là: ", tinh)