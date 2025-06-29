# Function to simulate infinity
def infinity():
    return 9999999  # large number as ∞

def dijkstra_algorithm():
    V = input("Enter all vertex names separated by space: ").split()
    n = len(V)

    # Initialize weight matrix with ∞
    w = {}
    for u in V:
        w[u] = {}
        for v in V:
            if u == v:
                w[u][v] = 0
            else:
                w[u][v] = infinity()

    e = int(input("Enter number of edges: "))
    print("Enter edges as: u v weight")
    for _ in range(e):
        u, v, wt = input().split()
        wt = int(wt)
        w[u][v] = wt
        w[v][u] = wt  # Remove this line for directed graphs

    u = input("Enter the source node: ")

    # Initialize S and distances
    S = [u]
    d = {}

    for v in V:
        if v == u:
            d[v] = 0
        else:
            d[v] = w[u][v]

    # Main loop
    while len(S) < len(V):
        # Choose node y in V - S such that d[y] is minimum
        min_dist = infinity()
        y = None
        for v in V:
            if v not in S and d[v] < min_dist:
                min_dist = d[v]
                y = v

        if y is None:
            break  # All remaining nodes are unreachable

        S.append(y)

        # Update distances
        for v in V:
            if v not in S:
                d[v] = min(d[v], d[y] + w[y][v])

    # Print final distances
    print("\nShortest distances from source node", u)
    print("Vertex\tDistance")
    for v in V:
        print(f"{v}\t{d[v] if d[v] != infinity() else '∞'}")

# Run the function
dijkstra_algorithm()
