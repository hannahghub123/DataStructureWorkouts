#  class to define a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None                    # initializing the head as None

    #  function to insert node as sepcific postion
    def push_at_pos(self, pos, data):
        if pos<1:                           # check if value of position is less than 0
            return
        
        new_node = Node(data)               # create new node
        if pos == 1:                        # if position is 1
            new_node.next = self.head       # assigning the head node as new node's next node
            self.head = new_node            # assigning the new node as the head node
            return
        
        current = self.head                 # set head node as the current node
        count = 0

        # iterate till the node before the specified position
        while current is not None and count < pos-1:
            current = current.next
            count+=1

        if current is None:
            return
        
        new_node.next = current.next        # assigning the current node's next node as new node's next node
        current.next = new_node             # assigning the new node as the current node's next node

    # function for list traversal
    def traversal(self):
        current = self.head                 # assigning the head node as current node

        while current:
            print(current.data, end=" -> ")
            current = current.next          # iterating to next node

        print("None")

l = Linkedlist()
l.head = Node(10)

l.push_at_pos(1,14)                         # func call for inserting node to specific position
l.push_at_pos(2,20)
l.push_at_pos(3,30)
l.push_at_pos(4,40)

l.traversal()                               # func call for list traversal