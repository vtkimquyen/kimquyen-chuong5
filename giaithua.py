# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:50:02 2024

@author: Kim Quyên
"""

n=int(input("Nhập số nguyên dương: "))

if n == 0:
    print("1")
else:
    giai_thua=1
    for i in range(1, n+1):
     giai_thua *= i
    print(f"Giai thừa của số là {n}! = {giai_thua}")