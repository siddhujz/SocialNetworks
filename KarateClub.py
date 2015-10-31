import networkx as nx
import matplotlib.pyplot as plt

def find_disjoint_graphs(my_graph):
    #Dictionary of edges with the calculated value of betweenness centrality
    edgeList = nx.edge_betweenness_centrality(my_graph)

    maxEdgeBetweenness = 0
    edgeNodes = ()

    # Loop over items and unpack each item, find maxEdgeBetweenness among all items.
    for node_id, edgeBetweennessVal in edgeList.items():
        #print("EdgeBetweenness = %f " % edgeBetweennessVal)
        #print("EdgeNodes = %s" % (node_id,))
        if edgeBetweennessVal > maxEdgeBetweenness:
            maxEdgeBetweenness = edgeBetweennessVal
            edgeNodes = node_id
    print("Highest betweenness is %f - for the edge %s" % (maxEdgeBetweenness, edgeNodes,))

    #Remove the edge with highest betweenness
    my_graph.remove_edge(edgeNodes[0], edgeNodes[1])
    print("Removed edge %s" % (edgeNodes,))
    #Add the removed edge to the edges_removed list
    edges_removed.append(edgeNodes)

    num_of_connected_components = nx.number_connected_components(my_graph)
    print("Number of connected components(sub-graphs/communities) after removing edge %s = %d" % (edgeNodes,num_of_connected_components))
    G = my_graph
    # Draw and show the graph, with labels
    nx.draw_networkx(my_graph, pos=None, with_labels=True)
    plt.show()


#Create a karate club graph
G = nx.karate_club_graph()
edges_removed = []
#Check if the Graph is disjoint
while nx.number_connected_components(G) < 2:
    find_disjoint_graphs(G)

print "List of edges removed from the graph to become disjoint = ", edges_removed

my_components = list(nx.connected_components(G))
print "The components are:"
for x in my_components:
    print list(x)
