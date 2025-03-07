class Node:
    def __init__(self,data):
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

    def find_index(self,data):                      # func call to find index of node
        current=self.head
        index=0
        while current:
            if current.data==data:
                print("index= ",index)              # obtain the index of the node
                return

            current=current.next
            index+=1

        raise KeyError("Element Not found")

l = Linkedlist()

l.push(1)                                           # func call for insertion
l.push(45)
l.push(5)
l.push(10)

l.display()                                         # func call for traversal
l.find_index(5)