# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:04:16 2024

@author: Kim Quyên
"""

n=int(input("Nhập vào số lẻ để tính (1*2*3*..*n): "))
tinh=1
for i in range(1, n+1):
    tinh = tinh*i
print("Kết quả là: ",tinh)