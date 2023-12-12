def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x<=pivot]
        greater = [x for x in arr[1:] if x>pivot ]

        return quicksort(less) + [pivot] + quicksort(greater)
    

mylist = [10,5,7,3,5,6,9]
sortedlist = quicksort(mylist)
print(sortedlist)