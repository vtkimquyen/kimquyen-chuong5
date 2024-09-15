# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:48:30 2024

@author: Kim Quyên
"""

n = int(input("Nhập vào số nguyên dương n để tính(1 + 2 + 3 + ... + n) "))
tinh = 0
for i in range (1, n + 1):
    tinh += i
print("Kết quả là: ",tinh)