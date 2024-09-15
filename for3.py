# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:21:45 2024

@author: Kim Quyên
"""
import random
ds=''
for i in range(random.randrange(1,12)):
    so = random.randrange(20,31)
    chuoi = str(so)
    ds= ds + chuoi + ''
print(ds)
ds = ds[:-1]
x = ds.split('')
print(len(x))