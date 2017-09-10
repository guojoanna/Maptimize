# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 04:12:38 2017

@author: dariu
"""

import os 
import csv
import GoogleRoute

def getTimes(fileA, fileB):
    #os.chdir('C:\\Users\\Ronan Perry\\Documents\\JHU\\Medhacks\\Python Scripts')
    os.chdir('C:\\Users\\dariu\\OneDrive - Johns Hopkins University\\Documents\\MedHacks')
    
    with open(fileA, encoding='utf-8-sig') as A:
        csvA = list(csv.reader(A))
    with open(fileB, encoding='utf-8-sig') as B:
        csvB = list(csv.reader(B))
        
    csvNew = []
    for j in csvA:
        min_time = GoogleRoute.route(j,csvB)
        if min_time == None:
            return csvNew
        else:
            csvNew.append(min_time)
        
    return csvNew
    
a = getTimes('latlongA.csv','Community_Health_Centers.csv')

with open('min_time_map.csv', 'w') as min_time_map:
    b = csv.writer(min_time_map, delimiter=',')
    b.writerows(a)
    min_time_map.close()
    
'''
with open('min_time.csv', 'w') as min_time:
    b = csv.writer(min_time, delimiter=',')
    B = []
    for i in a:
        C = i[0]
        if len(C) > 0:
            B.append(C)
    b.writerows(B)
    min_time.close()

with open('A_latlon.csv', 'w') as A_latlon:
    c = csv.writer(A_latlon, delimiter=',')
    E = []
    for i in a:
        C = i[0]
        #if len(C) > 0:
        E.append(C)
    c.writerows(E)
    A_latlon.close()    
    
with open('B_latlon.csv', 'w') as B_latlon:
    d = csv.writer(B_latlon, delimiter=',')
    G = []
    for i in a:
        F = i[4][5]
        #if len(F) > 0:
        G.append(F)      
    d.writerows(G)
    B_latlon.close() 
'''