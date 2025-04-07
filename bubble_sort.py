#algorithm
#  bubble_sort(a,n)
# {
#  for i=1 to n-1
#  for j=1 to n-i
#  if a[j]>a[j+1] then interchange (a[j],a[j+1])
# }

def bubble_sort(a, n):
    for i in range(n - 1):  
        for j in range(n - i - 1):  
            if a[j] > a[j + 1]:  
                a[j], a[j + 1] = a[j + 1], a[j]  

# Taking user input
n = int(input("Enter the number of elements: "))
a = list(map(float, input("Enter the elements separated by space: ").split()))

bubble_sort(a, n)
print("Sorted array:", a)
