# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:48:23 2024

@author: Kim Quyên
"""

import random
so_hiep = int(input("nhập vào số lần muốn chơi với máy: "))

hiep = 0
hoa = 0
diem_nguoi = 0
diem_may = 0
while hiep < so_hiep:
    nguoi_ra = input("Bạn ra cái gì (kéo, búa, bao): ")
    may_ra = random.choice(['kéo', 'búa', 'bao'])
    hiep = hiep + 1
    
    print("\tHiệp: ", hiep)
    print("\tNgười ra: ", nguoi_ra)
    print("\tMay ra: ", may_ra)
    if nguoi_ra == may_ra:
        hoa = hoa + 1
        print("\tKết quả hiệp này: Hòa")
    elif (nguoi_ra == 'kéo' and may_ra == 'bao') or\
         (nguoi_ra == 'búa' and may_ra == 'kéo') or\
         (nguoi_ra == 'bao' and may_ra == 'búa'):
        diem_nguoi = diem_nguoi + 1
        print("\tKết quả hiệp này: Người thắng")
    else:
        diem_may = diem_may + 1
        print("\tKết quả hiệp này: Máy thắng")
    print(f"\tĐiểm người: {diem_nguoi}   Điểm máy: {diem_may}   Hòa: {hoa}")
    continue
