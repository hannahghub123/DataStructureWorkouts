'''
Initializing arr along with an extra element 0 
to allocate the memory space for adding the new element
'''
arr = [10, 20, 30, 40, 50, 0]
n = 5
new_element = 25

print("Array before insertion: ")
for i in range(n):
    print(arr[i], end=" ")

''' 
Shifting the exiting elements to the next element position 
to empty the first element position
'''
for i in range(n-1, -1, -1):
    arr[i+1] = arr[i]

# inserting the first element
arr[0] = new_element

'''
in-built method - 
arr.insert(0, new_element)
'''

print("\nArray after insertion: ")
for i in range(n+1):
    print(arr[i], end=" ")