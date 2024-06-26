"""
networkx
DOC: https://networkx.org/documentation/stable/tutorial.html

ネットワーク図を表示したい時に使われる
"""
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_node(1)

G.add_nodes_from([2, 3])

G.add_edge(1, 2)
G.add_edge(2, 3)

nx.draw(G)
plt.show()