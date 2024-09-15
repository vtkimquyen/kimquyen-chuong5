# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:53:07 2024

@author: Kim Quyên
"""

n = int(input("Nhập vào số nguyên n để tính(1/2 + 3/4 + ... + (2n+1)/(2n+2): "))
tinh = 0
for i in range (0, n + 1):
    tinh += ((2 * i) + 1) / ((2 * i) + 2)
print("Kết quả là: ",tinh)