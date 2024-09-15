# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:01:29 2024

@author: Kim Quyên
"""

import random
n = int(input("Nhập số lượng số ngẫu nhiên n: "))

tong = 0
nhonhat = 10**9
lonnhat = 10**9

for i in range(n):
    songaunhien = random.random()
    tong += songaunhien
    if songaunhien < nhonhat:
        nhonhat = songaunhien
    if songaunhien > lonnhat:
        lonnhat = songaunhien

trungbinh = tong / n

print("Giá trị trung bình: {:.4f}".format(trungbinh))
print("Giá trị nhỏ nhất: {:.4f}".format(nhonhat))
print("Giá trị lớn nhất: {:.4f}".format(lonnhat))

        
    

