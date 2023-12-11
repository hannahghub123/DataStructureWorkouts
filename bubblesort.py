def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True

        if swapped == False:
            break

    return arr

arr = [1,55,8,45,73,13,2]
sortedlist = bubblesort(arr)

print(sortedlist)