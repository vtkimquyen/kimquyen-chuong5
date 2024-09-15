# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:20:43 2024

@author: Kim Quyên
"""

print("liệt kê tất cả bộ nghiệm nguyên của: 2x + 7y + 9z = 979 với x, y, z > 0 và x + y + z lớn nhất")
max_sum = 0
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 110):         
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z
                if tong > max_sum:  
                    max_sum = tong
                    so_lon_nhat = [x, y, z]
print("Bộ nghiệm có tổng các nghiệm lớn nhất là",so_lon_nhat,"với tổng =",max_sum)