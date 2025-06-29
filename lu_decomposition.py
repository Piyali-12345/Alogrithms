def lu_decompose(A):
    n = len(A)
    L = [[0.0]*n for _ in range(n)]
    U = [[0.0]*n for _ in range(n)]

    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            sum_u = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_u

        # Lower Triangular
        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_l = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_l) / U[i][i]

    return L, U

# -------------------------------
# USER INPUT SECTION
# -------------------------------

n = int(input("Enter the size of square matrix: "))
print("Enter the matrix row by row:")

A = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

L, U = lu_decompose(A)

# Output
print("\nLower Triangular Matrix L:")
for row in L:
    print(["{:.2f}".format(x) for x in row])

print("\nUpper Triangular Matrix U:")
for row in U:
    print(["{:.2f}".format(x) for x in row])
