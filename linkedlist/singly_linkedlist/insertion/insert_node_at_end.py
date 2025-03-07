#  class to define a node
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head = None

    # function to insert elements at the end of the list
    def push(self,data):
        new_node=Node(data)                         # create a new node
        if self.head is None:
            self.head=new_node                      # if there is no head node, assign the new node as head
        else:
            current=self.head                       # assign the head node as current node
            while current.next:                     # if current.next node exists the loop runs
                current=current.next

            current.next=new_node 

    # function for traversing through nodes
    def display(self):
        current=self.head                           # assigning the head node as current node
        while current:
            print(current.data,end="->")
            current=current.next                    # iterating to next node

        print("None")


l = Linkedlist()
l.push(1)
l.push(45)
l.push(5)
l.push(10)

l.display()