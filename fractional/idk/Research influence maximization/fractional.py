# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:09:52 2019

@author: puruk123
"""

import numpy as np
from Golub_Jackson import Golub_Jackson

def calc_C_bar(n,C): 
    C_bar = np.zeros((n,n))
    col_sums = np.sum(C,axis = 0)
    for i in range(n):
        C_bar[i,i] = 1 - col_sums[i]
    return C_bar 

def calc_A(n,C): 
    C_bar = calc_C_bar(n,C)
    A = np.dot(C_bar, np.linalg.inv(np.eye(n)-C)) #want to change
    return A


def init_active(x,theta): 
    S = []
    for i in range(len(x)): 
        S.append(max(x[i]-theta[i],0))
            
    return S

def F (M,S): 
    A = calc_A(M.n,M.C)
    AB = np.dot(A,M.B)
    influence = np.dot(AB,S)
    
        
    return new_S 

def calc_cascade (M,S,x): 
    active = []
    influence = x 
    while set(F(M,S)) == {0}:
        active.append(F(M,S))
        influence = influence + F(M,S)
       
    return influence

    
def sigma(x,mc,theta): 
    for i in range (mc): 
        S = init_active(x,theta)
        influence = calc_cascade(M,S,x)
    
    return influence
    


def greedy(M, mc): 
    budget = M.budget 
    theta = np.random.randint(M.theta_min, M.theta_max, size = (M.n))
    index = 0
    min = M.theta_max
    for i in range(theta):
        if theta(i) < min: 
            min = theta(i)
            index = i
            
    x = np.zeros(M.n)
    for i in range(theta): 
        x[index] = min
        
    greedy = 0
    while budget > 0:
        if sigma(x,theta,mc) > greedy: 
            t = sigma(x,theta,mc)
            greedy = t
            budget = budget - x.sum()
            min_x = M.theta_max
            for i in range (theta): 
                if x(i) - theta(i) < min_x:
                    x[i] = theta(i) - x(i)
                    
    return x
            
            
    
    
    
    

    