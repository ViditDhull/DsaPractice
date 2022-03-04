def rearrange(arr):
    arr1 = []
    for i in arr:
        if i <0:
            arr1.append(i)
    for i in arr:
        if i>=0:
            arr1.append(i)

    return arr1

#Example 
array = [-1,1,5,7,-4,4,-5,7,-2,1,-1]
print(rearrange(array))