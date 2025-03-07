'''
Time Complexity
O(N) → Since we traverse the list once.
Space Complexity
O(1) → Since we only use three pointers (prev, current, nextnode), no extra memory is used.
'''


class Node:                                         #  class to define a node
    def __init__(self, data):
        self.data=data
        self.next=None

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

    def display(self):                              # func for list traversal
        if self.head is None:                       # check if head exists
            print("None")
            return
        
        current=self.head                           # assigning the head node as current node
        while current:
            print(current.data,end="->")
            current=current.next                    # iterating to next node

        print("None")

    def reverse_linkedlist(self):
        prev=None
        current=self.head

        while current:
            nextnode = current.next                 # Store the next node
            current.next = prev                     # Reverse the current node's pointer
            prev = current                          # Move prev to current
            current = nextnode                      # Move current to nextnode

        self.head=prev


l = Linkedlist()
l.push(1)
l.push(45)
l.push(5)
l.push(10)

l.display()
print("Head: ",l.head.data)

l.reverse_linkedlist()

l.display()
print("Head: ",l.head.data)
