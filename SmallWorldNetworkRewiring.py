# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:18:13 2015

@author: SiddhuJz
"""

import networkx as nx
import matplotlib.pyplot as plt

avg_clustering_coefficient_list = []
diameter_list = []
probability_list = []
for x in range(0, 100):
#for x in range(0, 2):
    p = x/100
    #watts_strogatz_graph(n, k, p, seed=None)
    G = nx.watts_strogatz_graph(5000, 6, p, seed=None)

    avg_clustering_coefficient =  nx.average_clustering(G)
    print("(i) The average clustering coefficient with p = %f is %f" % (p,avg_clustering_coefficient))

    diameter = nx.diameter(G, e=None)
    print("(ii) The diameter of this network with p = %f is %d" % (p,diameter))

    if avg_clustering_coefficient < 0.01:
        break
    else:
        avg_clustering_coefficient_list.append(avg_clustering_coefficient)
        diameter_list.append(diameter)
        probability_list.append(p)

fig = plt.figure()

axis1 = fig.add_subplot(211)
axis1.set_xlabel('average clustering coefficient')
axis1.set_ylabel('probability p')
axis1.plot(avg_clustering_coefficient_list, probability_list)

axis2 = fig.add_subplot(212)
axis2.set_xlabel('diameter')
axis2.set_ylabel('probability p')
axis2.plot(diameter_list, probability_list)

plt.show()
