# algorithm
# Qsort(m, n) {
# if (m < n then {
# key = a(m); i = m; j = n+1;
# loop {
# repeat i = i+1 until a[i] key;
# repeat j = j-1 until a[j] key;
# if i < j then interchange(a(i), a(j));
# else break;
# }forever
# interch(a(m), a(j));
# Qsort(m, j-1);
# Qsort(j+1, n);
# }
# }

def quick_sort(a, m, n):
    if m < n:
        key = a[m]  
        i = m
        j = n + 1

        while True:
            i += 1
            while i <= n and a[i] < key:
                i += 1
            j -= 1
            while j >= m and a[j] > key:
                j -= 1

            if i < j:
                a[i], a[j] = a[j], a[i]  
            else:
                break
            a[m], a[j] = a[j], a[m]

        quick_sort(a, m, j - 1)
        quick_sort(a, j + 1, n)


# Taking user input
n = int(input("Enter the number of elements: "))
a = list(map(float, input("Enter the elements separated by space: ").split()))

quick_sort(a, 0, n - 1)
print("Sorted array:", a)


