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
    X = np.concatenate(np.zeros((M.n,M.n)))
    for key in S:
        X[key] = S[key]
    
    influence = np.dot(AB,np.split(X,M.n))
    
        
    return influence


def calc_cascade(M,S,theta): 
    A = {}
    for i in range(len(theta)):
        if F(M,S)[i]>theta[i]: 
            A[i] = theta[i]
                
    return A 

def sigma(M,S,theta):
    active = S 
    influence = F(M,S)
    while len(active) == 0: 
        new_S = calc_cascade(active, theta)
        active = new_S
        influence = np.add(influence, F(M,new_S))
        
        
    return influence

def calc_theta(M,mc):
    thetas = []
    for i in range(mc):
        theta = np.random.uniform(M.theta_min, M.theta_max, size=(M.n,M.n))
        thetas.append(theta)
    theta_final = [sum(x)/len(thetas) for x in zip(*thetas)]

            
    return theta_final

def greedy(M,mc):
    budget = M.budget 
    S = {}
    theta = np.concatenate(calc_theta(M, mc))
    print(theta)
    greedy = 0
    new = theta[:]
    while budget > 0:
        test = {}
        for x in new:
            print(new)
            index = list(theta).index(x)
            test[index] = x
            print(test)
            influence = sigma(M,test,theta) 
            print(np.sum(influence))
            if np.sum(influence) > greedy:
                S.update(test)
            greedy = np.sum(influence)
            budget = budget - x
            new = list(set(theta) - set(S.values()))
            test = {} 
            
               
            
    return S

Dp = np.array([1,1,1])
C = np.array([[1,2],[3,4]])
n = C.shape[0]
beta = np.array([[1,3],[0.5,0.5]])
B = np.diag(beta)
theta_min = 0
theta_max = 4
budget = 6

M = Golub_Jackson(n,Dp, C, B, theta_min, theta_max, budget)

def simulate_cascade (M): 
   
   return greedy(M,1000)


    
    
