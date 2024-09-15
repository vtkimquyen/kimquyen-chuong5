# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:45:25 2024

@author: Kim Quyên

a = int(input("Nhập độ dài cạnh a: "))
b = int(input("Nhập độ dài cạnh b: "))
c = int(input("Nhập độ dài cạnh c: "))
if a <= 0 or b <= 0 or c <= 0:
    print("Không phải là tam giác")
if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải là tam giác")
 
if a == b == c:
    print("Tam giác đều")
elif a == b or a == c or b == c:
    print("Tam giác cân")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Tam giác vuông")
else:
    print("Tam giác thường")

"""

a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))
c = int(input("Nhập vào số nguyên dương c: "))
cac_loai = [(a == b == c, "Đây là tam giác đều."),
    (a == b or b == c or a == c, "Đây là tam giác cân."),
    (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2, "Đây là tam giác vuông."),
    (a + b > c and a + c > b and b + c > a, "Đây là tam giác thường.")]
for dieu_kien, tam_giac in cac_loai:
    if dieu_kien:
        print(tam_giac)
        break
else:
    print("Đây không phải là tam giác")