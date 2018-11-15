#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:11:44 2018

@author: Mac
"""
#In lecture, we used maximum likelihood and a likelihood ratio test to complete a t-test.
#We can actually use a likelihood ratio test to compare two models as long as one model 
#is a subset of the other model. For example, we can ask whether y is a hump-shaped vs. 
#linear function of x by comparing a quadratic (a + bx + cx2) vs. linear (a + bx) model. 

#Generate a script that evaluates which model is more appropriate for the data in data.txt.

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import norm
from scipy.stats.distributions import chi2
from plotnine import *

df = pd.read_csv("data.txt", header = 0, sep = ",")

#Function to get negative log likelihood for linear model
def nll_linear(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    
    expected = B0+B1*obs.x
    nll = -1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll
#Guess for linear model
guess_linear = np.array([1,1,1])

#Function to get negative log likelihood for exponential model
def nll_exponential(p,obs):
    B0=p[0]
    B1=p[1]
    B2=p[2]
    sigma=p[3]
    
    expected= B0 + B1*obs.x + B2*obs.x*obs.x
    nll = -1*norm(expected,sigma).logpdf(obs.y).sum()
    return nll
#Guess for exponential model
guess_exponential = np.array([1,1,1,1])

#Gets negative log likelihood for linear model
linear_L = nll_linear(guess_linear,df)
#Gets negative log likelihood for exponential model
exponential_L = nll_exponential(guess_exponential,df)

#Function to take the likelihood ratio
def likelihood_ratio(llmin, llmax):
    return(2*(llmax-llmin))

#defining variables as likelihood ratios
    
#a is the likelihood ratio of linear over exponential
a=likelihood_ratio(linear_L,exponential_L)
#b is the likelihood ratio of exponential over linear
b=likelihood_ratio(exponential_L,linear_L)

#takes the p value for this test of linear over exponential, lower should be better
p = chi2.sf(a,1)
print('p: %5f' % p)

if(p < .05):
    print("The linear model is a better fit than the exponential model with the above p value")
else:
    print("The exponential model is a better fit than the linear model with the above p value")

#Output:
#199603.38342
#17007562.975
#p: 0.000000
#p2: 1.000000

