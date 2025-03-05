arr = [10, 29, 30, 75, 99]
target = 30

# searching for an element in an array using a for loop
for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at position ", i+1)
        break


'''
Application of Array traversal: Search an element in an array

Time complexity - O(n)
Auxiliary space - O(1)

'''