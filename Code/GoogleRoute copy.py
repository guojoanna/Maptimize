# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 02:49:11 2017

@author: Ronan Perry
"""
import requests
#from apiclient.discovery import build
#service = build('api_name', 'api_version')

def route(start, ends):
    key = 'AIzaSyAmR6MD9gVDxfu5wYOw19wUHCvh1NWyIl8'
    params = [('key=%s' % key),
              'mode=transit',
              'transit_mode=bus']
    origin = ('origins=%s,%s' % (start[0], start[1]))
    destination = 'destinations='
    for x in ends:
        destination = ('%s%s,%s|' % (destination, x[0], x[1]))
    destination = destination[:-1]
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?' + origin + '&' + destination
    for x in params:
        url = url + '&' + x
    print(url)
    r = requests.get( url )

    data = r.json()
    minimum = -1
    time = 0
    for val in data['rows'][0]['elements']:
        time = int(val['duration']['value'])
        print(time)
    if minimum < 0:
        minimum = time
    elif time < minimum:
        minimum = time
    return minimum

if __name__ == '__main__':
        route([39.299518, -76.594204], [[39.312781, -76.595294], [39.312781, -76.595294]])