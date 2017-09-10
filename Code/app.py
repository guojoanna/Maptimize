# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:54:18 2017

@author: dariu
"""

from flask import Flask, send_from_directory, render_template

app_directory = 'C:\\Users\\dariu\\OneDrive - Johns Hopkins University\\Documents\\MedHacks\\transit_map'
allowed_extensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['app_directory'] = app_directory

def allowed_file(map):
    return '.' in map and \
           map.rsplit('.', 1)[1] in allowed_extensions

@app.route('/show/<map>') #decorator, insert filename.jpg
def update_map(map):
    map = 'http://127.0.0.1:5000/uploads/' + map
    return render_template('template.html', map = map)
    
@app.route('/uploads/<map>')
def send_file(filename):
    return send_from_directory(app_directory, map)
    
if __name__ == '__main__': 
    app.run()