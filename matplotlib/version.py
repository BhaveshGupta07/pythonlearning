import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
graph = nx.Graph()

# Take input from the user to add elements to the dictionary
while True:
    vertex = input("Enter a vertex (or press Enter to stop): ")
    if not vertex:
        break
    
    adjacent_vertices = input(f"Enter adjacent vertices for '{vertex}' (separated by spaces): ").split()
    graph.add_node(vertex)
    for adj_vertex in adjacent_vertices:
        graph.add_edge(vertex, adj_vertex)

# Display the created dictionary representing the undirected graph
print("\nDictionary representing the undirected graph (adjacency list):")
print(graph.adj)

# Draw the graph
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()