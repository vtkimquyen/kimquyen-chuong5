# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:05:56 2024

@author: Kim Quyên
"""

n=int(input("Nhập một số: "))
dic = {i: i**i for i in range(1, n+1)}
print(dic)