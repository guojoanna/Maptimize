# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 12:43:31 2017

@author: dariu
"""
from min_path import getTimes
import csv

fileA = 'latlongA.csv'
fileB = 'Community_Health_Centers.csv'

with open('min_time_map.csv', encoding='utf-8-sig') as A:
        set1 = list(csv.reader(A))

newB = getTimes(fileA,fileB)
with open('min_time_map_new.csv', 'w') as map_new:
    b = csv.writer(map_new, delimiter=',')
    b.writerows(newB)
    map_new.close()
    
with open('min_time_map_new.csv', encoding='utf-8-sig') as B:
        set2 = list(csv.reader(B))
       
set3 = []
for i in set1:
    if set2[i] < i:
        C = set2[i]
        set3.append(C)
    else:
        D = i
        set3.append(D)

with open('min_time_map_optimized.csv', 'w') as optimized:
    c = csv.writer(optimized, delimiter=',')
    c.writerows(set3)
    optimized.close()
    





    
'''
with open(fileB, encoding='utf-8-sig') as B:
        fileB = list(csv.reader(B))
        
        run = []
fileB_flat = [item for sublist in fileB for item in sublist]

for i in range(len(fileB)):
    run.append = getTimes(fileA, fileB_flat[i] +'.csv')
print(run)
'''