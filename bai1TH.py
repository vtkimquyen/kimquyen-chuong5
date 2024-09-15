# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:14:16 2024

@author: Kim Quyên
str_input = input("Nhập chuỗi: ")
dodaichuoi = len(str_input)
print("Độ dài chuỗi: ", dodaichuoi)
kitudacbiet = 0 
kituthuong = 0
kituso = 0
kituhoa = 0

kitudacbiet=  set("!@#$%^&*()-=+/")

for kitu in str_input:
    if kitu in kitudacbiet:
        kitudacbiet += 1
    elif kitu.islower():
        kituthuong += 1
    elif kitu.isdigit():
        kituso += 1
    elif kitu.upper():
        kituhoa += 1
print("Số kí tự đặc biệt: ", kitudacbiet)
print("Số kí tự [a-z]: ", kituthuong)
print("Số kí tự [0-9]: ", kituso) 
print("Số kí tự chữ [A-Z]: ", kituhoa) 
"""

chuoi = input("Nhập vào một chuỗi: ")
len(chuoi)
ky_tu_db = '!@#$%^&*()-=+./'
day_ky_tu_db = [i for i in chuoi if i in ky_tu_db]
print(day_ky_tu_db)
print(len(day_ky_tu_db))
       
ky_tu_thuong = [e for e in chuoi if e.islower()]
print(ky_tu_thuong)
print(len(ky_tu_thuong))

ky_tu_so = [s for s in chuoi if s.isdigit()]
print(ky_tu_so)
print(len(ky_tu_so))
    
ky_tu_hoa = [h for h in chuoi if h.isupper()]
print(ky_tu_hoa)
print(len(ky_tu_hoa))

