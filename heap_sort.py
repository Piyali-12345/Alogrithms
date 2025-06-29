def max_heapify(A, i, heap_size):
    l = 2 * i
    r = 2 * i + 1
    largest = i

    if l <= heap_size and A[l] > A[largest]:
        largest = l

    if r <= heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Swap
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    heap_size = len(A) - 1
    for i in range(heap_size // 2, 0, -1):
        max_heapify(A, i, heap_size)

def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A) - 1

    for i in range(heap_size, 1, -1):
        A[1], A[i] = A[i], A[1]  # Swap max with last element
        heap_size -= 1
        max_heapify(A, 1, heap_size)

# -------------------------------
# USER INPUT AND EXECUTION BELOW
# -------------------------------

# Take input from user
user_input = input("Enter the elements to sort (space-separated): ")
arr = list(map(float, user_input.strip().split()))

# Convert to 1-indexed array by adding dummy at index 0
A = [0] + arr

print("\nOriginal Array:", A[1:])

heap_sort(A)

print("Sorted Array (Ascending):", A[1:])
