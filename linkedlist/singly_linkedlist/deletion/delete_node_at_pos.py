class Node:                                         #  class to define a node
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None                              # initialize head as None

    def insert_node(self, data):                            # function to insert elements
        new_node=Node(data)                         # create a new node
        if self.head is None:
            self.head=new_node                      # if there is no head node, assign the new node as head
        else:
            current=self.head                       # assign the head node as current node
            while current.next:                     # if current.next node exists the loop runs
                current=current.next

            current.next=new_node                   # link new node to current node

    def delete_node_at_pos(self, pos):
        # case 1: check if list is empty
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        if pos == 1:                                #  check if position is 1, set new node as head
            self.head = current.next
            return
            
        count = 1
        while current and count<pos-1:              # iterate till position-1 node
            current = current.next
            count+=1

        if not current or not current.next:         # check if position exists
            print("pos not found")
            return

        temp = current.next                         # set next node as temp node
        current.next = temp.next                    # assign next of temp node as next node

        del temp                                    # delete temp node

    def traversal(self):                            # func call for list traversal
        if self.head is None:                       # check if head exists
            print("None")
            return
        
        current=self.head                           # assigning the head node as current node
        while current:
            print(current.data,end="->")
            current=current.next                    # iterating to next node

        print("None")


l = Linkedlist()

l.insert_node(10)                                   # func call for insertion
l.insert_node(20)
l.insert_node(30)
l.insert_node(40)
l.traversal()                                       # func call for traversal

l.delete_node_at_pos(5)                             # func call for deletion
l.traversal()