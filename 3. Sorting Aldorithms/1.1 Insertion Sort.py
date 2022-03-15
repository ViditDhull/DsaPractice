def insertion_sort(a):
    for i in range(1, len(a)):
        curNum = a[i]
        for j in range(i-1, 0, -1):
            if a[j] > curNum:
                a[j+1] = a[j]
            else:
                a[j+1] = curNum
                break