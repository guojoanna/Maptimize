# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:31:52 2017

@author: dariu
"""
import matplotlib.pyplot as plt
from conversion_list import convert_list


population = convert_list('histogram',1)
population = [float(x) for x in population]

transit_time = convert_list('histogram',0)
transit_time = [float(y) for y in transit_time]
 
plt.bar(transit_time,population,align='center', alpha=0.5,width=50)
plt.xlabel('Transit Time (sec)')
plt.ylabel('Population (people)')
plt.title('Transit times to nearest health centers for people without vehicles')
 
plt.show()
plt.savefig('histogram.png')