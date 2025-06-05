def bellman_ford(edges, num_vertices, start):
    dist = [float('inf')] * num_vertices
    dist[start] = 0

    for _ in range(num_vertices - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            print("Graf obsahuje záporný cyklus.")
            return None

    return dist

# Testovací data
edges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 4),
    (3, 1, -6)

]

num_vertices = 4
start = 0

result = bellman_ford(edges, num_vertices, start)

if result:
    for i, d in enumerate(result):
        print(f"Vzdálenost z vrcholu {start} do vrcholu {i}: {d}")
