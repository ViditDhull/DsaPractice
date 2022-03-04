def sort_array(arr):
    arr1 = []
    zero = arr.count(0)
    one = arr.count(1)
    for i in range(len(arr)):
        if zero!= 0:
            arr1.append(0)
            zero -=1
        elif one != 0:
            arr1.append(1)
            one -=1
        else:
            arr1.append(2)

    return arr1

#Example
array = [0,1,2,1,0,1,2,2,0,0]
print(sort_array(array))
