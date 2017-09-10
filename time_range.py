# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:11:06 2017

@author: dariu
"""

from min_path import getTimes
import os

os.chdir('C:\\Users\\dariu\\OneDrive - Johns Hopkins University\\Documents\\MedHacks')

'''
fileA = input('Name of point A file: ') + '.csv'
fileB = input('Name of point B file: ') + '.csv'
'''
fileA = 'latlongA1.csv'
fileB = 'Community_Health_Centers.csv'

min_times = getTimes('latlongA1.csv','Community_Health_Centers.csv')

a = min_times.sort()
print(a)