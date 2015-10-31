import networkx as nx
import matplotlib.pyplot as plt

def plot_degree_distribution(G):
    degs = {}
    for n in G.nodes():
        deg = G.degree(n)
        if deg not in degs:
            degs[deg] = 0
        degs[deg] += 1

    items = sorted(degs.items())
    #print "items: ", items
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([k for (k,v) in items], [v for (k,v) in items])

    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.title("Degree  Distribution of the generated graph")

    #plt.plot([degs[])
    xx = []
    yy = []
    for (k,v) in items:
        if k == 1:
            xx.append(k)
            yy.append(v)
        if v == 1:
            xx.append(k)
            yy.append(v)             
            break
    plt.plot(xx, yy)

    #print "xx = ", xx
    #print "yy = ", yy
    slope = (yy[1] - yy[0])/(xx[1] - xx[0])
    #print "slope = ", slope

    print "The approx. overlapping of both the plots indicate that it follows a power law graph"
    print "Estimated r value = ", -slope

    #As N(k) = c*(k^-r)
    #c = degs(1)
    
    plt.show()
    fig.savefig("my_degree_distribution.png")

#nx.barabasi_albert_graph(n, m, seed=None)

#barabasi albert graph with 1000 nodes, and preferential attachment as 1
G1 = nx.barabasi_albert_graph(1000, 1, seed=None)

# Draw and show the graph
nx.draw(G1)
plt.show()

#Initialize Largest Degree in the graph to zero
maxDegree1 = 0
for x in range(0, 1000):
    #print "Degree of %d = %d" % (x, G.degree(x))
    if G1.degree(x) > maxDegree1:
        maxDegree1 = G1.degree(x)
print "Max Degree with n:1000 = %d" % (maxDegree1)

#barabasi albert graph with 2000 nodes, and preferential attachment as 1
G2 = nx.barabasi_albert_graph(2000, 1, seed=None)
maxDegree2 = 0
for x in range(0, 2000):
    if G2.degree(x) > maxDegree2:
        maxDegree2 = G2.degree(x)
print "Max Degree with n:2000 = %d" % (maxDegree2)

#barabasi albert graph with 5000 nodes, and preferential attachment as 1
G3 = nx.barabasi_albert_graph(5000, 1, seed=None)
maxDegree3 = 0
for x in range(0, 5000):
    if G3.degree(x) > maxDegree3:
        maxDegree3 = G3.degree(x)
print "Max Degree with n:5000 = %d" % (maxDegree3)

#Plot Degree Distribution of the generated graph
plot_degree_distribution(G1)

