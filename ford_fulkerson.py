def bfs(residual_graph, s, t, parent):
    visited = {node: False for node in residual_graph}
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for v in residual_graph[u]:
            if not visited[v] and residual_graph[u][v] > 0:
                parent[v] = u
                visited[v] = True
                queue.append(v)
                if v == t:
                    return True
    return False

def ford_fulkerson(G, capacity, s, t):
    # Initialize residual graph
    residual_graph = {}

    # Ensure all nodes exist in residual_graph
    for u in G:
        residual_graph[u] = {}

    for u in G:
        for v in G[u]:
            # Forward capacity
            residual_graph[u][v] = capacity[(u, v)]
            # Ensure reverse edge exists
            if v not in residual_graph:
                residual_graph[v] = {}
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0

    # Initialize flow
    flow = {}
    for u in G:
        for v in G[u]:
            flow[(u, v)] = 0
            flow[(v, u)] = 0  # Reverse flow

    parent = {}
    max_flow = 0

    while bfs(residual_graph, s, t, parent):
        # Step 5: find bottleneck capacity
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u

        # Step 6-8: update flow and residual graph
        v = t
        while v != s:
            u = parent[v]
            flow[(u, v)] += path_flow
            flow[(v, u)] -= path_flow
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow, flow

# -------------------------------
# USER INPUT SECTION
# -------------------------------
G = {}
capacity = {}

n = int(input("Enter number of vertices: "))
print("Enter vertex names separated by space:")
nodes = input().split()

for node in nodes:
    G[node] = []

e = int(input("Enter number of edges: "))
print("Enter edges as (u v capacity):")
for _ in range(e):
    u, v, c = input().split()
    c = int(c)
    G[u].append(v)
    if v not in G:
        G[v] = []
    capacity[(u, v)] = c

s = input("Enter source node: ")
t = input("Enter sink node: ")

# Run Ford-Fulkerson
max_flow, flow = ford_fulkerson(G, capacity, s, t)

print("\n Maximum Flow:", max_flow)
print("\n Flow along each edge:")
for (u, v) in flow:
    if (u, v) in capacity:
        print(f"{u} -> {v} : {flow[(u, v)]}")
