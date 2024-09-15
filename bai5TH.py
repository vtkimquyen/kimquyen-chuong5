# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:49:48 2024

@author: Kim Quyên
"""

import random
so_nguoi_choi = random.randint(8, 20)
print("Số lượng người tham gia chơi: ", so_nguoi_choi)
ds_nguoi_choi = [f"Người chơi {i}" for i in range(1,so_nguoi_choi +1)]
so_hiep = int(input("nhập vào số hiệp bạn muốn chơi với máy: "))
hoa = 0
diem_nguoi_choi = [0] * so_nguoi_choi
for hiep in range(1, so_hiep + 1):
    print(f"Hiệp thứ {hiep}")
    nguoi_choi_ra = [random.choice(['kéo', 'búa', 'bao']) for _ in range(so_nguoi_choi)]
    for i in range(0,so_nguoi_choi):
        print(f"{ds_nguoi_choi[i]} ra {nguoi_choi_ra[i]}")
    so_keo = nguoi_choi_ra.count('kéo')
    so_bua = nguoi_choi_ra.count('búa')
    so_bao = nguoi_choi_ra.count('bao')
    if (so_keo > 0 and so_bua > 0 and so_bao > 0) or\
       (so_keo > 0 and so_bua == 0 and so_bao == 0) or\
       (so_keo == 0 and so_bua > 0 and so_bao == 0) or\
       (so_keo == 0 and so_bua == 0 and so_bao > 0):
        hoa = hoa + 1
        print("\tKết quả hiệp này: Hòa")
    elif so_keo > 0 and so_bua == 0:
        for i in range(so_nguoi_choi):
            if nguoi_choi_ra[i] == 'kéo':
                diem_nguoi_choi[i] += 1
        print("\tKết quả hiệp này: Kéo thắng")
    elif so_bua > 0 and so_bao == 0:
        for i in range(so_nguoi_choi):
            if nguoi_choi_ra[i] == 'búa':
                diem_nguoi_choi[i] += 1
        print("\tKết quả hiệp này: Búa thắng")
    elif so_bao > 0 and so_keo == 0:
        for i in range(so_nguoi_choi):
            if nguoi_choi_ra[i] == 'bao':
                diem_nguoi_choi[i] += 1
        print("\tKết quả hiệp này: Bao thắng")
print("Kết quả sau các hiệp là:")
for i in range(so_nguoi_choi):
    print(f"{ds_nguoi_choi[i]} được {diem_nguoi_choi[i]} điểm")
print(f"Số hiệp hòa là: {hoa}")
