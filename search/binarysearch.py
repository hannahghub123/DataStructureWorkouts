'''
Complexity Analysis of Binary Search:

Time Complexity: 
Best Case: O(1)
Average Case: O(log N)
Worst Case: O(log N)

Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(logN).
'''

def binarysearch(arr,l,r,x):

    #enter the loop only if left index is less than or equal to the right index
    while l<=r: 

        mid = l + (r-l)//2 #finding mid value of the given array

        if arr[mid] == x: #checking if mid value equals to the required number
            return mid 
        
        elif x<arr[mid]: #checking if the required number is lesser than the obtained mid-value
            r = mid-1

        else:
            l = mid + 1

    return -1 #return -1 if no element is found

arr = [2, 3, 4, 10, 40]
x = 10

result = binarysearch(arr,0,len(arr)-1,x)

if result == -1:
    print("Element not found")
else:
    print("Result found at position - ",result+1)

