#  class to define a node
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    # function to insert elements at the end of the list
    def push(self, data):
        new_node=Node(data)                         # create a new node
        if self.head is None:
            self.head=new_node                      # if there is no head node, assign the new node as head
        else:
            current=self.head                       # assign the head node as current node
            while current.next:                     # if current.next node exists the loop runs
                current=current.next

            current.next=new_node                   # assigning the new node as the last node

    # func to insert node at beginning
    def push_at_start(self, data):
        new_node=Node(data)                         # create new node
        new_node.next=self.head                     # link head to new node
        self.head=new_node                          # set new node as head

    def display(self):
        if self.head is None:
            return
        
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next

        print('None')


l = Linkedlist()

l.push(1)
l.push(45)
l.push(5)
l.push(10)
l.display()

l.push_at_start(11)
l.display()