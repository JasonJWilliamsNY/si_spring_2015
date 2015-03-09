# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:56:19 2015

@author: jasonwilliams
"""
#import some special pyton functions
import pandas as pd
from scipy import stats as sp

#Create a dictionary to hold the observations

observed_mnm = {}

# Ask the user about each color and store the input
''' M&M Colors:
Brown, Blue, Red, Orange, Yellow, Green

'''

observed_mnm['Brown']=  float(raw_input('How many Brown M&Ms? \n'))
observed_mnm['Blue']=   float(raw_input())



#turn the observed_mnm dictionary into a dataframe so we can do math

data = pd.DataFrame.from_dict(observed_mnm, orient ='index')

print data


# add the name 'observed' to the dataframe
#data.columns = ['observed'] 

# convert the observations to percentages

#data = data / data.sum()

# add an 'expected' column and fill in with 

#data['expected'] = ''


'''
data.expected['Blue'] = 0.24
data.expected['Brown'] = 0.13
data.expected['Green'] = 0.16
data.expected['Yellow'] = 0.14
data.expected['Red'] = 0.13
data.expected['Orange'] = 0.20

print data
'''

# Use the stats package to do the ChiSquare test
#result = sp.stats.chisquare(data.observation,data.expected,ddof=4)
#print result
