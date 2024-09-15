# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:58:22 2024

@author: Kim Quyên
"""

print("Tính x + (x^2)/(1+2) + (x^3)/(1+2+3) ... + (x^n)/(1+2+3+...+n)")
x = float(input("Nhập vào số x: "))
n = int(input("Nhập vào số nguyên n: "))
tinh = 0
n_tang = 0
for i in range (1, n + 1):
    n_tang += i
    tinh += (x ** i) / n_tang
print("Kết quả là: ",tinh)