'''
Complexity Analysis of Linear Search:

Time Complexity:
Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
Average Case: O(N)

Auxiliary Space: O(1) as except for the variable to iterate through the list, no other variable is used. 
'''

def linearsearch(arr,num):
    n = len(arr)
    for i in range(n):
        if arr[i] == num: #simple linear search
            return i
        
        
arr = [42, 5, 8,55, 10]
print("Here is the array - ",arr)
num = int(input("which element is to be found from this arry ? "))
result = linearsearch(arr, num)

if result:
    print("Element is found in position ",result+1)
else:
    print("Element not found")


