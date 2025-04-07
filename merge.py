#algorithm
# merge_sort(a,p,r){
#     if p<r then{
#         q=(p+r)/2;
    
#     merge_sort(a,p,q);
#     merge_sort(a,q+1,r);
#     merge_sort(a,p,q,r);
# }
# }




def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    left = arr[p:q+1]
    right = arr[q+1:r+1]

    i = 0  
    j = 0  
    k = p 

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Take input from user
user_input = input("Enter numbers separated by space: ")
arr = list(map(float, user_input.strip().split()))

merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
