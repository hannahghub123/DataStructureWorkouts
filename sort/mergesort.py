def mergesort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    lefthalf = mergesort(lefthalf)
    righthalf = mergesort(righthalf)

    return merge(lefthalf,righthalf)

def merge(left, right):
    result = []
    i = j = 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [78,2,45,4,95,11,53,6,77,100]
sortedlist = mergesort(arr)

print(sortedlist)
