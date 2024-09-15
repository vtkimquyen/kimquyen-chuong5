# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:59:58 2024

@author: Kim Quyên
"""
n = int(input("Nhập vào số nguyên dương N: "))
while n<0:
        n=int(input("Đây không phải là số nguyên. Vui lòng nhập lại."))
else: 
            
    for i in range(1, n + 1):
        if n % i == 0:
            uoc=i
            print("Các ước của số là: ", uoc) 