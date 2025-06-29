def enqueue(Q, value):
    Q.append(value)

def dequeue(Q):
    return Q.pop(0)

def BFS(G, s):
    color = {}
    d = {}
    p = {}
    Q = []

    # Initialization
    for u in G:
        if u != s:
            color[u] = "WHITE"
            d[u] = float('inf')
            p[u] = None
    color[s] = "GRAY"
    d[s] = 0
    p[s] = None
    enqueue(Q, s)

    # BFS traversal
    print("\nBFS Traversal starting from:", s)
    while len(Q) > 0:
        u = dequeue(Q)
        print("Visiting:", u)
        for v in G[u]:
            if color[v] == "WHITE":
                color[v] = "GRAY"
                d[v] = d[u] + 1
                p[v] = u
                enqueue(Q, v)
        color[u] = "BLACK"

    # Displaying results
    print("\nVertex\tDistance\tParent")
    for u in G:
        distance = d[u] if u in d else '∞'
        parent = p[u] if u in p else 'NIL'
        print(f"{u}\t{distance}\t\t{parent}")

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
print("Enter edges (u v):")
for _ in range(e):
    u, v = input().split()
    G[u].append(v)
    G[v].append(u)  # For undirected graph

s = input("Enter source/start node for BFS: ")

# Run BFS
BFS(G, s)
