def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        minvalue = arr[i]
        index = i
        for j in range(i+1,n):
            if arr[j]<minvalue:
                minvalue=arr[j]
                index=j

        arr[i],arr[index]=arr[index],arr[i]

    return arr

mylist = [10,5,7,3,5,6,9]
sortedlist = selectionsort(mylist)
print(sortedlist)