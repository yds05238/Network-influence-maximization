# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:10:16 2019

@author: puruk123
"""

import numpy as np
import networkx as nx 

class Golub_Jackson(object):
    """Attributes:
       D = n x m matrix, Dik >= 0, share of value of asset k held by organization i
       p = asset price vector
       C = n x n cross holding matrix 
       beta = default cost 
       index = index of the graph object created with numbered indexes 
       theta_min = min possible theta value
       theta_max = max possible theta value
    """
    
    def __init__(self, G, Dp, C, beta, theta_min, theta_max, budget):
        self.n = C.shape[0]
        self.Dp = Dp
        self.C = C
        self.B = np.diag(beta)
        self.theta_min = theta_min
        self.theta_max = theta_max
        self.budget = budget
        self.G = nx.from_numpy_matrix(C)
        
        #throwing exception when dimensions of theta and C don't match up 
       

   

"""Test_cases
D = np.array([1,1,1])
p = 2
C = np.array([[0,0],[0,0]])
beta = np.array([0.5,0.5])

D1 = np.array([0,1,2])
p1 = 1
C1 = np.array([[0,1],[1,0]])
beta1 = np.array([0.23,0.84])

D2 = np.array([3,5,2])
p2 = 5
C2 = np.array([[0,3],[5,0]])
beta2 = np.array([3,5])
i = Golub_Jackson(D, p, C, beta, 0, 1)
j = Golub_Jackson(D1,p1,C1,beta1,-0.4, 2.3)
k = Golub_Jackson(D2,p2,C2,beta2, -2, 0.6)


G1 = nx.Graph()
G1.add_node(0,data = i)
G1.add_node(1,data = j)
G1.add_node(2, data = k)
G1.add_edge(0,1)
print(G1.node[2]['data'].Dp)
"""

