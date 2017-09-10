# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 09:00:00 2017

@author: dariu
"""

import json
from pprint import pprint

with open('citydata.json') as data_file:    
    data = json.load(data_file)

data[234363251]