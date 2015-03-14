# -*- coding: utf-8 -*-

"""
Created on Mon Mar 9 14:56:19 2015
@author: jasonwilliams
"""
#import some special pyton functions
import pandas as pd

import scipy.stats.mstats as mst

#Create a dictionary to hold the observations
observed_mnm = {}
# Ask the user about each color and store the input
observed_mnm['Brown']   =  float(raw_input('How many Brown M&Ms? \n'))
observed_mnm['Blue']    =  float(raw_input('How many Blue M&Ms? \n'))
observed_mnm['Red']     =  float(raw_input('How many Red M&Ms? \n'))
observed_mnm['Orange']  =  float(raw_input('How many Orange M&Ms? \n'))
observed_mnm['Yellow']  =  float(raw_input('How many Yellow M&Ms? \n'))
observed_mnm['Green']   =  float(raw_input('How many Green M&Ms? \n'))
#turn the observed_mnm dictionary into a dataframe so we can do math
data = pd.DataFrame.from_dict(observed_mnm, orient ='index')
# add the name 'observed' to the dataframe
data.columns = ['observed']
# sum up the observations
observations = data.observed.sum()

# convert the observations to percentages
#data = data / data.sum()
# add an 'expected' column and fill in with
data['expected'] = ''
data.expected['Blue']   = 0.24  * observations
data.expected['Brown']  = 0.13  * observations
data.expected['Green']  = 0.16  * observations
data.expected['Yellow'] = 0.14  * observations
data.expected['Red']    = 0.13  * observations
data.expected['Orange'] = 0.20  * observations
print data
# Use the stats package to do the ChiSquare test
result = mst.chisquare(data.observed,data.expected)
print "Chi-squared statistic is %f" %result[0]
print "p-value is: %f" %result[1]
print "Probability null hypothesis is true: %f%%" %(float(result[1])*100)


if  (float(result[1])*100) > 5:
    print "You should accept the null hypthothesis!"
else:
    print "You should reject the null hypthothesis!" 