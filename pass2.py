# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:54:00 2024

@author: Kim Quyên
"""

sochan = [ sochan for sochan in range(2020, 3839) if sochan % 2 == 0]
ds = [ds for ds in sochan if ds % 9 == 0]
print(*ds, sep='\t')