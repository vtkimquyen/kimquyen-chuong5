# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:07:55 2024

@author: Kim Quyên
"""
x = int(input("Nhập số nguyên x: "))
y = int(input("Nhập số nguyên y: "))

while y != 0:
  a=x%y
  x=y
  y=a

print("Ước chung lớn nhất của hai số là: {}".format(x))
