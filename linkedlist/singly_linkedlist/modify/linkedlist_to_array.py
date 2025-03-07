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
        self.head=None                              # initialize head as None

    def push(self,data):                            # function to insert elements
        new_node=Node(data)                         # create a new node
        if self.head is None:
            self.head=new_node                      # if there is no head node, assign the new node as head
        else:
            current=self.head                       # assign the head node as current node
            while current.next:                     # if current.next node exists the loop runs
                current=current.next

            current.next=new_node                   # link new node to current node

    def traversal(self):
        if self.head is None:                       # check if head exists
            print("None")
            return
        
        current=self.head                           # assigning the head node as current node
        while current:
            print(current.data,end="->")
            current=current.next                    # iterating to next node

        print("None")

    def count_nodes(self):
        current = self.head
        count = 0

        while current:                              # traverse the list to get the length
            count+=1
            current = current.next

        return count

    def linkedlist_to_array(self):
        current = self.head
        n = self.count_nodes()
        arr = [0]*n

        for i in range(n):                          # traverse the list to store the node values as array elements
            arr[i] = current.data
            current = current.next

        print(arr)


l = Linkedlist()

l.push(10)                                           # func call for insertion
l.push(20)
l.push(30)
l.push(40)
l.push(50)
l.traversal()                                       # func call for traversal

l.linkedlist_to_array()
