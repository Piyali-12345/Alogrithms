def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    for L in range(2, n + 1):  # L is the chain length
        for i in range(0, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# Interactive input from user
print("Matrix Chain Multiplication")
n = int(input("Enter the number of matrices: "))
print(f"Enter {n + 1} dimensions (for {n} matrices A1 to A{n}):")

p = []
for i in range(n + 1):
    val = int(input(f"p[{i}] = "))
    p.append(val)

m, s = matrix_chain_order(p)

print("\nMinimum number of multiplications needed:")
print(m[0][n - 1])

print("\nOptimal parenthesization:")
print_optimal_parens(s, 0, n - 1)
print()
