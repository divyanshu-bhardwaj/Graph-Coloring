# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx
import ipywidgets as widgets

G = nx.Graph()

no_of_nodes = int(input("Enter the no of nodes : "))

G.add_nodes_from([1,no_of_nodes])

no_of_edges = int(input("Enter the no of Edges : "))

edges = list()
for i in range(0,no_of_edges):
    node1 = int(input("START "+str(i)+" : "))
    node2 = int(input("END   "+str(i)+" : "))
    print()
    edges.append((node1,node2));
print(edges)

G.add_edges_from(edges)

nx.draw(G, with_labels=True)

colouring = nx.greedy_color(G, strategy='largest_first', interchange=False)

def draw_coloring(G,coloring,colors):
    fig = plt.figure()
    n_colors = len(colors)

    pos = nx.spring_layout(G)

    for i in range(no_of_nodes):
        nx.draw_networkx_nodes(G,pos,[i+1],node_color = colors[colouring[i+1]])
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
    
    plt.axis('off')
    plt.show() 
    return fig

some_colors = ['red','blue','green','yellow','purple']

fig2 = draw_coloring(G,colouring,some_colors)

nodes = list(G.nodes)
print(nodes)

edges = list(G.edges)
print(edges)

color_lists = []
color_of_edge = []

for i in range(len(nodes)+1):
    color_lists.append([])
    color_of_edge.append(-1)
print('List of lists:')
print(color_lists)

def getSmallestColor(ls1,ls2):
    i = 1
    while(i in ls1 or i in ls2):
        i = i +1
    return i

i = 0
for ed in edges:
    newColor = getSmallestColor(color_lists[ed[0]],color_lists[ed[1]])
    color_lists[ed[0]].append(newColor)
    color_lists[ed[1]].append(newColor)
    color_of_edge[i] = newColor
    i = i+1

print(color_of_edge)

G = nx.Graph()
print(edges)
for i in range(len(edges)):
    print(edges[i][0])
    G.add_edge(edges[i][0],edges[i][1],color=some_colors[color_of_edge[i]-1])
print(G.edges)

colors = nx.get_edge_attributes(G,'color').values()

pos = nx.circular_layout(G)
nx.draw(G, pos, 
        edge_color=colors, 
        with_labels=True,
        width=2)

no_of_faces = len(edges)+2-len(nodes)-1
print(no_of_faces)

def regionColour(regions):
    print("NO OF FACES : "+str(regions))
    for i in range(1,regions+1):
        print("FACE 1 : "+some_colors[i%4])

regionColour(no_of_faces)