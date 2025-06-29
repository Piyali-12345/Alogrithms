# Global variables to be used inside DFS_VISIT
color = {}
parent = {}
pre = {}
post = {}
time = 0

# DFS_VISIT procedure
def DFS_VISIT(u, Adj):
    global time
    color[u] = "GRAY"
    time += 1
    pre[u] = time

    for v in Adj[u]:
        if color[v] == "WHITE":
            parent[v] = u
            DFS_VISIT(v, Adj)

    color[u] = "BLACK"
    time += 1
    post[u] = time

# DFS main procedure
def DFS(G):
    global time
    time = 0
    for u in G:
        color[u] = "WHITE"
        parent[u] = None

    for u in G:
        if color[u] == "WHITE":
            DFS_VISIT(u, G)

    # Output results
    print("\nDFS traversal completed.\n")
    print("Vertex\tPre\tPost\tParent")
    for u in G:
        print(f"{u}\t{pre[u]}\t{post[u]}\t{parent[u]}")
        
# ----------------------------
# USER INPUT SECTION
# ----------------------------

G = {}
n = int(input("Enter number of vertices: "))
print("Enter vertex names separated by space:")
vertices = input().split()

for v in vertices:
    G[v] = []

e = int(input("Enter number of edges: "))
print("Enter edges as u v (directed edge from u to v):")
for _ in range(e):
    u, v = input().split()
    G[u].append(v)

# Call DFS on the user-defined graph
DFS(G)
