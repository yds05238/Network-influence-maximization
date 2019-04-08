# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:34:51 2019

@author: puruk123
"""

import numpy as np
import networkx as nx
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


def F_of_V (n,C,B,x,theta): 
    A = calc_A(n,C)
    AB = np.dot(A,B)
    active = np.zeros(n)
    for i in range(len(x)): 
        if x[i] > theta[i]:
            active[i] = 1  
    active_list = []
    new_x = np.dot(AB,active)

           
    return new_x

def calc_cascade(M,x,S,theta): 
    active = S[:]
    A = S[:]
    while active:
        temp = F_of_V(M.n, M.C, M.B, x,theta) 
        x = temp
        active = list(temp[1])
        A.append(active)
        
    return [x,A]
        
def sigma(M, x, S, mc): 
    x_list = []
    S_list = []
    for i in range(mc): 
        theta = np.random.randint(M.theta_min, M.theta_max, size = (M.n))
        temp = calc_cascade(M,x,S,theta)
        x_list.append(temp[0])
        S_list.append(temp[1])
    
    return [np.mean(x_list), S_list, theta]
                    
def greedy(M, mc): 
    x = np.zeros(M.n)
    S = []
    budget = M.B
    while (M.budget > np.sum(x)):
        s = sigma(M,x,S,mc)
        if len(s[1]) > len(S): 
            x = s[2] - s[0]
            budget = budget - np.sum(x)
            S = s[1]
            
    return (x,S)


Dp = np.array([1,1,1])
C = np.array([[1,2],[3,4]])
n = C.shape[0]
beta = np.array([[1,3],[0.5,0.5]])
B = np.diag(beta)
theta_min = 0
theta_max = 2
budget = 4

M = Golub_Jackson(n,Dp, C, B, theta_min, theta_max, budget)

def simulate_cascade (M): 
   
   return greedy(M,10)


    
    
    
    