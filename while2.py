# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:29:51 2024

@author: Kim Quyên
"""

so=float(input("Nhập số trong khoảng [-89.9; 88.8]: "))
while -89.9<=so<=88.8:
    print("Số bạn nhập hợp lệ")
    break
else:
    print("Giá trị không thuộc phạm vi [-89.9; 88.8]. Vui lòng thử lại.")