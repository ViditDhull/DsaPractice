from re import A


def Kth_max(arr, k):
    for i in range(k-1):
        a = arr.index(max(arr))
        arr.pop(a)

    return max(arr)

def Kth_min(arr,k):
    for i in range(k-1):
        a = arr.index(min(arr))
        arr.pop(a)

    return min(arr)

#Example
array1 = [10,20,30,40,60,50,100,80]
print(Kth_max(array1, 5))
print(Kth_min(array1, 3))