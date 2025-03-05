arr = [10, 20, 30, 40, 0]
n= 4
element = 50

print("Array before insertion: ")
for i in range(n):
    print(arr[i], end=" ")

arr[n] = element

'''
in-built method - 
arr.append(element)
'''

print("\nArray after insertion: ")
for i in range(n+1):
    print(arr[i], end=" ")