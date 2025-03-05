arr = [10, 20, 30, 20, 20, 40, 50]
ele = 20
n = len(arr)
pos = None

print("Array before deletion: ",*arr)

for i in range(n):
    if arr[i] == ele:
        pos = i
        break

for i in range(pos+1, n):
    arr[i-1] = arr[i]

arr.pop()

'''
built-in method -

if ele in arr:
    arr.remove(ele)
    
'''

print("Array after deletion: ",*arr)