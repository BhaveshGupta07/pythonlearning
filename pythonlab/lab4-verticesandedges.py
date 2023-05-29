graphs={}
nodes=int(input("enter the number of nodes in the graph "))
for i in range(nodes):
    vertex = input("Enter a vertex (or 'done' to finish): ")
    if vertex == "done":
        break
    
    neighbors = input(f"Enter neighbors for vertex '{vertex}' (separated by spaces): ").split()
    graphs[vertex] = neighbors


print(graphs)