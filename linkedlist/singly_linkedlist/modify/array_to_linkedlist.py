'''
Time complexity - O(N), We traverse the array once (O(N) time).
Space Complexity - O(N), We create N new nodes (O(N) space).
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def array_to_linkedlist(self, arr):        
        if not arr:                                 # Handle empty array case
            return

        self.head = Node(arr[0])                    # Set head to the first element
        current = self.head

        for i in range(1, len(arr)):
            new_node = Node(arr[i])                 # Create a new node
            current.next = new_node                 # Link the current node to the new node
            current = new_node  

    def traversal(self):
        if self.head is None:                       # check if head exists
            print("None")
            return
        
        current=self.head                           # assigning the head node as current node
        while current:
            print(current.data,end="->")
            current=current.next                    # iterating to next node

        print("None")

l = Linkedlist()

arr = [10, 20, 30, 40, 50]

l.array_to_linkedlist(arr)
l.traversal()