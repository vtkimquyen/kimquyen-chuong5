# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:31:41 2024

@author: Kim Quyên
"""

n=int(input("Nhập số vào để tính (1/2 + 1/4 +..+ 1/2n): "))
tinh=0
for i in range(1, n+1):
    tinh += 1/(2*i)
print("Kết quả là: ", tinh)