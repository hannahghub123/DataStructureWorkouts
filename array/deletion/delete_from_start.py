arr = [10, 20, 30, 40, 50]
n = len(arr)

print("Array before deletion: ")
for i in range(n):
    print(arr[i], end=" ")

# Shifting the exiting elements to the left
for i in range(1, n):
    arr[i-1] = arr[i]

# deleteing the last element
arr.pop()

'''
in-built method - 
del arr[0]
'''

print("\nArray after deletion: ")
print(*arr)

