from ast import While


def union(arr1,arr2):
    arr3 = []
    for i in arr1:
        arr3.append(i)
    for i in arr2:
        arr3.append(i)
    for i in arr3:
        while arr3.count(i)>1:
            arr3.pop(arr3.index(i))
    return arr3

def intersection(arr1,arr2):
    arr3 = []
    for i in arr1:
        if i in arr2:
            arr3.append(i)
    for i in arr3:
        if arr3.count(i)>1:
            arr3.pop(arr3.index(i))
    return arr3

#Example
array1 = [2,4,6,8,4,8,2]
array2 = [4,6,7,8,9,7,5,33,2]
print(union(array1,array2))
print(intersection(array1,array2))