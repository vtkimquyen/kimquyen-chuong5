# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:37:27 2024

@author: Kim Quyên
"""

danh_sach=[]
for so in range(2018, 2829):
    if so % 2 == 0 and so % 5 == 0:
        danh_sach.append(so)
print(danh_sach)
        