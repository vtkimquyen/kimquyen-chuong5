# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:21:00 2024

@author: Kim Quyên


"""


n=int(input("Nhập số nguyên dương: "))
tong=0
while n>0:
   chu_so=n%10
   tong += chu_so
   n//=10
print("Tổng các chữ số là: ", tong)
         