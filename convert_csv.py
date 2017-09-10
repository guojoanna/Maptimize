# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:46:53 2017

@author: dariu
"""
import os
import csv

os.chdir('C:\\Users\\dariu\\OneDrive - Johns Hopkins University\\Documents\\MedHacks')

txt_file = r"latlongA.txt"
csv_file = r"latlongA.csv"

in_txt = csv.reader(open(txt_file, "r"), delimiter = ',')
latlongA_csv = csv.writer(open(csv_file, "w"))

latlongA_csv.writerows(in_txt)

