# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:36:23 2024

@author: Kim Quyên
"""

n=int(input("Nhập số vào để tính (1 + 1/3 + 1/5 +..+ 1/(2n+1)): "))
tinh=0
for i in range(0, n+1):
    tinh += 1/((2*i) + 1)
print("Kết quả là:", tinh)