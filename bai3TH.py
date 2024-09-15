# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:46:15 2024

@author: Kim Quyên
"""

ID_User = input("Nhập vào ID của bạn: ")
while True:
    if len(ID_User) < 6 or len(ID_User) > 24:
        print("Độ dài ID từ 6 đến 24 ký tự")
        ID_User = input("\nNhập lại ID của bạn: ")
        continue

    ID_db = True
    ID_trang = True
    for i in ID_User:
        if i in '!@#$%^&*()-=+':
            ID_db = False
        if i == ' ':
            ID_trang = False
    if ID_trang == False:
        print("ID không chứa khoảng cách")  
            
    if ID_db == False:
        print("ID không chứa ký tự đặc biệt") 
    if ID_trang == False or ID_db == False:
        ID_User = input("\nNhập lại ID của bạn: ")
        continue        
    break

Password = input("Nhập vào mật khẩu: ")    
while True:
    if len(Password) < 6 or len(Password) > 24:
        print("Độ dài Pass từ 6 đến 24 ký tự")
        Password = input("\nNhập lại ID của bạn: ")
        continue

    Pass_az = False
    Pass_09 = False
    Pass_AZ = False
    Pass_db = False
    for p in Password:
        if p.islower():
            Pass_az = True
        if p.isdigit():
            Pass_09 = True      
        if p.isupper():
            Pass_AZ = True    
        if p in '$#@':
            Pass_db = True
    if Pass_az == False:
        print("Pass có ít nhất 1 chữ cái nằm trong [a-z]")
    if Pass_09 == False:
        print("Pass có ít nhất 1 số nằm trong [0-9]")
    if Pass_AZ == False:
        print("Pass có ít nhất 1 kí tự nằm trong [A-Z]")
    if Pass_db == False:
        print("Pass có ít nhất 1 kí tự nằm trong [$ # @]")
    if Pass_az == False or Pass_09 == False or Pass_AZ == False or Pass_db == False:
        Password = input("\nNhập lại Password của bạn: ")
        continue        
    break      
print("\nCHÀO MỪNG BẠN ĐẾN VỚI BÌNH NGUYÊN VÔ TẬN")        
