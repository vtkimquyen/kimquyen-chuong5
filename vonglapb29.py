# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:10:06 2024

@author: Kim Quyên
"""

import math

n = int(input("Nhập n: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if math.gcd(i, j) == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
