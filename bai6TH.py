# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:51:29 2024

@author: Kim Quyên
"""

import random
so_ve = int(input("Bạn muốn bao nhiêu vé số Vietlot: "))
tien_ve = 0
ds_cac_ve = []
for _ in range(1, so_ve + 1):
    tien_ve += 10000
    ve = []
    while len(ve) < 6:
        so = str(random.randint(1, 45))
        if so not in ve:
            ve += [so]
    ds_cac_ve += [ve]
n = 1
for i in ds_cac_ve:
    print(f"Vé thứ {n}: {'-'.join(i)}")
    n += 1
print(f"Tổng tiền mua vé số là: {tien_ve:,} đ")

ve_trung = []
while len(ve_trung) < 6:
    so_trung = str(random.randint(1, 45))
    if so_trung not in ve_trung:
        ve_trung += [so_trung]
print("\nVé số trúng thưởng là:",'-'.join(ve_trung))

tien_trung_thuong = 0
for a in ds_cac_ve:
    
    so_giong_ve_trung = 0
    for e in range(6):
        if a[e] == ve_trung[e]:
            so_giong_ve_trung += 1
            
    if so_giong_ve_trung == 3:
        tien_trung_thuong += 30000
    elif so_giong_ve_trung == 4:
        tien_trung_thuong += 300000
    elif so_giong_ve_trung == 5:
        tien_trung_thuong += 10000000
    elif so_giong_ve_trung == 6:
        tien_trung_thuong += 10000000000
print(f"Tổng số tiền trúng thưởng bạn nhận được: {tien_trung_thuong:,} đ")
    
    
    
    
    
