# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:11:11 2019

@author: puruk123
"""

import numpy as np
import networkx as nx 


f=nx.gnm_random_graph(10,30,directed=True)
nx.draw(f)

def simulate_cascade (f): 
   
   return greedy(f,2,p=0.3,mc=1000)

def greedy (G, k, p, mc = 1000):
    S = []
    for _ in range(k): 
        best = 0
        for j in set(range(G.number_of_nodes())) - set(S): 
            s = Integral_cascade(G, S + [j], p, mc)
            if s > best: 
                best = s 
                node = j 
        S.append(node)
    
    return (S)

''' Sigma '''
def Integral_cascade (G, S, p, mc = 1000):
    n = []
    for i in range(mc):
        active = S[:]   
        A = S[:] 
        while active: 
             neighbor_active = [] 
             for node in active: 
                 print(G.neighbors(node))
                 success = np.random.uniform(0,1,len(G.neighbors(node))) < p
                 neighbor_active += list(np.extract(success, G.neighbors(node)))
             active = list(set(neighbor_active) - set(A))
             A += active
        n.append(len(A))
        
    return (np.mean(n))


    
    
    
    
    
    
    