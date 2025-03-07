#  class to define a node
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None                              # initializing the head as None

    # function to insert elements at the end of the list
    def push_at_end(self,data):
        new_node=Node(data)                         # create a new node
        if self.head is None:
            self.head=new_node                      # if there is no head node, assign the new node as head
        else:
            current=self.head                       # assign the head node as current node
            while current.next:                     # if current.next node exists the loop runs
                current=current.next

            current.next=new_node                   # assigning the new node as the last node

    # function to insert node after a specific node
    def push_after_node(self,data,key):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current:
            if current.data==key:                   # checking if the value of current node matches with the key
                new_node.next=current.next          # assigning the current node's next node as new node's next node
                current.next=new_node               # assigning the new node as the current node's next node
                return
                
            current=current.next                    # iterating to the next node

    # function for traversing through nodes
    def display(self):
        current=self.head                           # assigning the head node as current node
        while current:
            print(current.data,end="->")
            current=current.next                    # iterating to next node

        print("None")


l = LinkedList()

l.push_at_end(1)                                    # function call for insertion at end
l.push_at_end(45)
l.push_at_end(5)
l.push_at_end(10)

l.display()                                         # function call for traversal

l.push_after_node(35,45)                            # function call for insertion after a specific node
l.display()

