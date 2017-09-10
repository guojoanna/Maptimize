# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:27:57 2017

@author: dariu
"""

import os 
import csv
os.chdir('C:\\Users\\dariu\\OneDrive - Johns Hopkins University\\Documents\\MedHacks')

def convert_list(filename,column):
    with open(filename + '.csv', encoding='utf-8-sig') as A:
            listA = list(csv.reader(A))
    
    B = []
    for i in listA:
        C = i[column]
        if len(C) > 0:
            B.append(C)
    return B
