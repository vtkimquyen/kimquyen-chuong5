# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:41:11 2024

@author: Kim Quyên
"""

email = input("Nhập vào một email: ")
if email.count('@') != 1:
    print("Email không hợp lệ.")
else:
    truoc, sau = email.split('@')
    if len(truoc) < 6:
        print("Email không hợp lệ: Phần trước @ phải có ít nhất 6 ký tự.")
    else:
        email_trang = True
        email_kt = True
        for i in truoc:
            if i == ' ':
                email_trang = False
            elif not i.isalnum():
                email_kt = False
        if email_trang == False:
            print("Email không hợp lệ: Phần trước @ chứa khoảng trắng.")
        if email_kt == False:
            print("Email không hợp lệ: Phần trước @ chứa ký tự đặc biệt.")
