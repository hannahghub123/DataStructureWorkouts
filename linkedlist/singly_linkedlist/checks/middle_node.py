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

    def display(self):                              # func for list traversal
        if self.head is None:                       # check if head exists
            print("None")
            return
        
        current=self.head                           # assigning the head node as current node
        while current:
            print(current.data,end="->")
            current=current.next                    # iterating to next node

        print("None")

    def middle_node(self):                          # func call to find middle node
        current_node = self.head
        slow=fast=current_node                      # set two pointers slow & fast as current node

        while fast and fast.next:                   # Ensure fast is not None and fast.next is not None
            slow = slow.next                        # Move slow pointer one step forward
            fast = fast.next.next                   # Move fast pointer two steps forward

        return slow.data
    

l = Linkedlist()
l.push(1)
l.push(45)
l.push(5)
l.push(10)
l.push(20)
l.push(100)
l.push(75)

l.display()
print(l.middle_node()," is the middle node")
