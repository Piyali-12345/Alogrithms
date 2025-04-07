# algorithm

# Selection_sort(a,n) {
# for i = 1 to n-1 do {
# j = i;
# for k = j+1 to n do
# if a(k) < a(j) then j = k;
# if i != j then intch(a(i), a(j));
# }
# }



def selection_sort(a, n):
    for i in range(n - 1):  
        j = i
        for k in range(i + 1, n):  
            if a[k] < a[j]:  
                j = k  
        if i != j:  
            a[i], a[j] = a[j], a[i]  

# Taking user input
n = int(input("Enter the number of elements: "))
a = list(map(float, input("Enter the elements separated by space: ").split()))

selection_sort(a, n)
print("Sorted array:", a)
