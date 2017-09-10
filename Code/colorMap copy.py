"""
Geographic C
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
from scipy.misc import imread

def colorMap(dataList, VERBOSE=False):

	# add debug print statements
	if VERBOSE:
		print "The dataList is:", dataList


# plot colormap of matrices
    	fig, ax = plt.subplots()
	min_val, max_val = 0, numPoints-1
	plt.matshow(mapMat, cmap=plt.cm.Blues)
	for i in xrange(numPoints):
		   	 for j in xrange(numPoints):
		   	 		c = mapMat[j,i]
		   	 		ax.text(i, j, str(c), va='center', ha='center')
	plt.show(block=True)

if __name__ == '__main__':
	listX = list(range(99))
	listY = list(range(99))

	import random
	listTimes = random.sample(xrange(500, 10001), 100)
	print listTimes

	dataList = [listX, listY, listTimes]

	bmap = imread('bmap.png')
	plt.imshow(bmap)
