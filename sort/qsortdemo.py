def qsort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x<=pivot]
        great = [x for x in arr[1:] if x>pivot ]

        return qsort(less) + [pivot] + qsort(great)
    
arr = [78,2,45,4,95,11,53,6,77,100]
sortedlist = qsort(arr)

print(sortedlist)