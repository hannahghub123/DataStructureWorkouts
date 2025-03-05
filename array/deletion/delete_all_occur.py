arr = [10, 20, 30, 20, 20, 40, 20, 50]
ele = 20

print("Array before deletion: ",*arr)

# keep the elements in the array except the elements that match the target
arr = [x for x in arr if x!= ele]

print("Array after deletion: ",*arr)
