# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:19:43 2024

@author: Kim Quyên
"""

n=int(input("Nhập vào số nguyên để tính (1 + 1/2 + 1/3 +..+ 1/n): "))
tinh=0
for i in range(1, n+1):
    tinh += 1/i
print("Kết quả là: ", tinh)