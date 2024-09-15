# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:37:19 2024

@author: Kim Quyên
"""

n = int(input("Nhập vào số nguyên dương n: "))
for i in range(2, n):
    if n % i == 0:
        print(n,"không phải là số nguyên tố")
        break
else:
    print(n,"là số nguyên tố")