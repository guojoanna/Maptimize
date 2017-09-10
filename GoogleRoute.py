# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 02:49:11 2017

@author: Ronan Perry
"""
import requests
global data
#from apiclient.discovery import build
#service = build('api_name', 'api_version')

def route(start, ends):
    key = 'AIzaSyDpe72tsrH6ascVrkBnN_j0pq0h_ywjHuI'
    params = [('key=%s' % key),
              'mode=transit',
              'transit_mode=bus',
              'departure_time=1504992237']
    origin = ('origins=%s,%s' % (start[0], start[1]))
    destination = 'destinations='
    for x in ends:
        destination = ('%s%s,%s|' % (destination, x[0], x[1]))
    destination = destination[:-1]
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?' + origin + '&' + destination
    for x in params:
        url = url + '&' + x
    #print(url)
    r = requests.get( url )
    
    data = r.json()
    minimum = -1
    min_val = -1
    count = 0
    time = 0
    try:
        for val in data['rows'][0]['elements']:
            time = int(val['duration']['value'])
            count = min_val + 1
            if minimum < 0:
                minimum = time
                min_val = count
            elif time < minimum:
                minimum = time
                min_val = count
        return [minimum,start,ends[count]]
    except Exception as e:
        print(e)
        print(data)
        return None
        
#shortest = route([39.299518, -76.594204], [[39.312781, -76.595294], [39.312781, -76.595294]])