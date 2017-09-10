"""
Geographic Color Map of Health Facility Access
Authors: Joanna Guo, Darius Irani, JungMin Lee, Ronan Perry, Hadley VanRenterghem
Name: colorMap
Date Created: September 9, 2017

Description: Generates color map given geometric pixel coordinates and corresponding access times

Inputs
1. dataList of 3 sublists: x geographic pixel coordinates, y geographic pixel coordinates
3. List of best times for each geographic point in seconds
4. VERBOSE (optional): debug inputs

Outputs:
1. Color map

"""

# Imports necessary for this function
import numpy as np
import math
import pandas as pd
import pyedflib
import matplotlib.pyplot as plt
import csv

def rgb2hex(r,g,b):
	hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
	return hex

def colorMap(dataList, bestTimes, VERBOSE=False):

	# add debug print statements
	if VERBOSE:
		print "verbose"

	bestTimesMax = max(bestTimes)
	print bestTimesMax
	scaledBest = []
	print len(bestTimes)
	for i in range(len(bestTimes)):
		scaledBest.append(float(bestTimes[i])/bestTimesMax)
	print scaledBest

	scaledColor = []
	for iScaled in range(len(scaledBest)):
		scaledColor.append(255*(1-scaledBest[iScaled]))

	return scaledColor

if __name__ == '__main__':
	hexScaled = []
	dataList = [[39.328,-76.608], [39.325,-76.608], [39.321,-76.608], [39.318,-76.608], [39.315,-76.608], [39.311,-76.608], [39.308,-76.608], [39.305,-76.608], [39.298,-76.608], [39.321,-76.603], [39.318,-76.603], [39.315,-76.603], [39.311,-76.603], [39.308,-76.603], [39.305,-76.603], [39.301,-76.603], [39.298,-76.603], [39.295,-76.603], [39.321,-76.599], [39.318,-76.599], [39.315,-76.599], [39.311,-76.599], [39.308,-76.599], [39.305,-76.599], [39.301,-76.599], [39.298,-76.599], [39.295,-76.599], [39.292,-76.599], [39.318,-76.595], [39.315,-76.595], [39.311,-76.595], [39.308,-76.595], [39.305,-76.595], [39.301,-76.595], [39.298,-76.595], [39.295,-76.595], [39.292,-76.595], [39.318,-76.59], [39.315,-76.59], [39.311,-76.59], [39.308,-76.59], [39.305,-76.59], [39.318,-76.586], [39.315,-76.586], [39.311,-76.586], [39.308,-76.586], [39.305,-76.586], [39.301,-76.586], [39.315,-76.582], [39.305,-76.582], [39.301,-76.582], [39.315,-76.577], [39.311,-76.577], [39.308,-76.577], [39.315,-76.573], [39.311,-76.573], [39.308,-76.573], [39.315,-76.569], [39.315,-76.565], [39.318,-76.56], [39.315,-76.56], [39.318,-76.556], [39.315,-76.556], [39.318,-76.552], [39.315,-76.552]]
	bestTimes = [748, 679, 628, 259, 288, 280, 414, 285, 295, 357, 1, 345, 486, 472, 403, 288, 380, 319, 268, 279, 322, 387, 527, 608, 581, 409, 160, 446, 373, 146, 523, 639, 414, 428, 309, 255, 568, 575, 349, 488, 322, 361, 747, 645, 396, 25, 385, 356, 455, 533, 483, 574, 789, 576, 430, 299, 335, 219, 199, 500, 208, 443, 627, 341, 817]
	
	scaledColor = colorMap(dataList, bestTimes, True)
	print(scaledColor)
	for i in range(len(scaledColor)):
		hexScaled.append(rgb2hex(255, int(scaledColor[i]), 0))
	print(hexScaled)

	# with open('hexScaled.csv', 'wb') as csvfile:
 #    		csvwriter = csv.writer(csvfile, delimiter=',')
 #    		for i in range(len(hexScaled)):
 #    			csvwriter.writecolumn(hexScaled)

    	hexScaled_df = pd.DataFrame(data=hexScaled[:])

    	# create CSV file of channel header names and data
        hexScaled_df.to_csv('hexScaled.csv', index=False, header=False)

    

