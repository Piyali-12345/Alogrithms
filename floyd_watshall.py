def floyd_warshall(W):
    n = len(W)
    # Initialize D with the initial weights
    D = [[W[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    return D

# -------------------------------
# USER INPUT SECTION
# -------------------------------

INF = float('inf')
n = int(input("Enter number of vertices: "))
print("Enter the weight matrix row by row. Use 'inf' for no edge:")

W = []
for i in range(n):
    row = input(f"Row {i+1}: ").split()
    W.append([INF if x == 'inf' else int(x) for x in row])

# Run Floyd-Warshall
result = floyd_warshall(W)

# Output result
print("\nAll-Pairs Shortest Path Matrix:")
for i in range(n):
    for j in range(n):
        print("∞" if result[i][j] == INF else result[i][j], end="\t")
    print()
