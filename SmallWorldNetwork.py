# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:53:49 2015

@author: SiddhuJz
"""

import networkx as nx

#watts_strogatz_graph(n, k, p, seed=None)
G = nx.watts_strogatz_graph(5000, 6, 0, seed=None)
avg_clustering_coefficient =  nx.average_clustering(G)
print("(i) The average clustering coefficient = %f" % avg_clustering_coefficient)

diameter = nx.diameter(G, e=None)
print("(ii) The diameter of this network = %d" % diameter)
