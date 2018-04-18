
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 05:26:15 2018

@author: priyanshu
"""



import numpy as np



s_0 = 40
sigma = .20
r= .06
t = 1 # in years

def stock_prices(s_0, sigma, r, t):
    
    m = 100000 # number of paths
    n = 100
    dt = t/n    
    
    st = np.zeros(m) + s_0
    
    z = np.random.normal(size=int(m/2))
    s = s_0 + s_0*(r*dt + sigma* np.sqrt(dt)*z)
    s2 = s_0 + s_0*(r*dt + sigma* np.sqrt(dt)*(-z)) # antithetic variation reduction
    s = np.hstack([s, s2])
    st = np.column_stack([st,s])
    
    for i in range(2,n+1):
        z = np.random.normal(size=int(m/2))
        s = st[:int(m/2),(i-1)]*(1 + r*dt + sigma*np.sqrt(dt)*z)
        s2 = st[int(m/2):,(i-1)]*(1 + r*dt + sigma*np.sqrt(dt)*(-z)) # antithetic variation reduction
        s = np.hstack([s,s2])
        #print(s.mean())
        st = np.column_stack([st, s]) 
        
    return(st)

st = stock_prices(s_0, sigma, r, 1)



















