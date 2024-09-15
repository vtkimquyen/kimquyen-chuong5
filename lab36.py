# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:52:33 2024

@author: Kim Quyên
"""

n=int(input("Nhập vào số nguyên dương để tính (1^2 + 2^2 + 3^2 + .. + n^2): "))
tinh = 0
for i in range(1, n+1):
    tinh += i**2
print("Kết quả là: ", tinh)