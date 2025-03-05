arr = [10, 20, 30, 40]
n = len(arr)
pos = 3

print("Array before deletion: ",*arr)

for i in range(pos, n):
    arr[i-1] = arr[i]

if pos <= n:
    arr.pop()

print("Array after deletion: ",*arr)