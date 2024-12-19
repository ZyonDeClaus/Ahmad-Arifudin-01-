# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:41:22 2024

@author: HP
"""

n = int(input("Masukkan nilai n :"))
total = 0
for i in range (1,n+1):
    total +=i
print(f"Jumlah bilangan dari 1 hingga {n} adalah {total}")