# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:43:22 2024

@author: Kim Quyên
"""

n=int(input("Nhập vào để tính (1/1*2 + 1/2*3 +..+ 1/n*(n+1): "))
tinh=0
for i in range(1, n+1):
    tinh += 1/(i*(i + 1))
print("Kết quả là: ", tinh)