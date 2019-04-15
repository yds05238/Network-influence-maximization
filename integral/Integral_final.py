# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:27:20 2019

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



def F (M,S): 
    A = calc_A(M.n,M.C)
    AB = np.dot(A,M.B)
    influence = np.multiply(AB,list(set(S.values())))
    
        
    return influence


def calc_cascade(M,S,theta): 
    A = {}
    for i in range(len(theta)):
        if F(M,S)[i]>theta[i]: 
            A[i] = theta[i]
                
    return A 

def sigma(M,S,theta,mc):
    for i in range(mc):
        active = S 
        influence = F(M,S)
        while len(active) == 0: 
            new_S = calc_cascade(active, theta)
            active = new_S
            influence = np.add(influence, F(M,new_S))
            
        
        return influence


def greedy(M,mc):
    budget = M.budget 
    S = {}
    theta = np.random.uniform(M.theta_min, M.theta_max, size = (M.n))
    while budget > 0: 
        test = {}
        greedy = 0
        new = set(theta) - set(S)
        for x in new:
            test[list(theta).index(x)] = x
            influence = sigma(M,test,theta,mc) 
            if np.sum(influence) > greedy: 
                S.update(test)
                greedy = np.sum(influence)
                budget = budget - np.sum(influence)
    
    return S 

Dp = np.array([1,1,1])
C = np.array([[1,2],[3,4]])
n = C.shape[0]
beta = np.array([[1,3],[0.5,0.5]])
B = np.diag(beta)
theta_min = 0
theta_max = 2
budget = 5

M = Golub_Jackson(n,Dp, C, B, theta_min, theta_max, budget)

def simulate_cascade (M): 
   
   return greedy(M,10)


    
    
