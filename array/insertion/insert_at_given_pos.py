''' Python program to insert given element 
at a given position in an array'''

arr = [10, 20, 30, 40, 0]
n = 4
new_element = 15
position = 3

print("Array before insertion: ")
for i in range(n):
    print(arr[i], end=" ")

# Shifting elements to the right
for i in range(n, position-1, -1):
    arr[i] = arr[i-1]
 
# Insert the new element at index pos - 1
arr[position-1] = new_element

'''
in-built method - 
arr.insert(pos-1, new_element)
'''

print("\nArray elements after insertion: ")
for i in range(n+1):
    print(arr[i], end=" ")