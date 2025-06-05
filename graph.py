import networkx as nx
import matplotlib.pyplot as plt

def bellman_ford(edges, num_vertices, start):
    dist = [float('inf')] * num_vertices
    dist[start] = 0
    predecessor = [None] * num_vertices

    for _ in range(num_vertices - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                predecessor[v] = u

    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            print("Graf obsahuje záporný cyklus.")
            return None, None

    return dist, predecessor

# Graf: hrany (u, v, váha)
edges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 4),
    #(3, 1, -6) # záporný cyklus deaktivován
]
num_vertices = 4
start = 0

dist, pred = bellman_ford(edges, num_vertices, start)

if dist:
    G = nx.DiGraph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)  # rozmístění uzlů

    # Kreslení uzlů
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # Kreslení hran
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

    # Popisky uzlů
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    # Popisky hran (váhy)
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(f"Bellman-Ford: vzdálenosti z vrcholu {start}\n{dist}")
    plt.axis('off')
    plt.show()
