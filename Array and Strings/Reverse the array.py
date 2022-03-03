def reverse_array(arr, start, end):
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
        
    return arr
#Example        
arr1 = [1,2,3,4,5,]
print(arr1)
print(reverse_array(arr1, 0, 4))
