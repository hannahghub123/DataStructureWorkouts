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

    def delete_after(self, prev_node):              # func for deleting node after a specific node
        current=self.head                           # set head as current node
        while current.next:
            # check if current node data matches the key & next node exists
            if current.data==prev_node and current.next:
                temp = current.next                 # set next node as temporary node
                current.next=temp.next              # assign next node of temp as the next node
                del temp                            # delete temp node
                break

            current=current.next                    # move to next node



l = Linkedlist()

l.push(1)                                           # func call for insertion
l.push(45)
l.push(5)
l.push(10)
l.push(2)
l.push(70)
l.display()                                         # func call for traversal

l.delete_after(45)                                  # func call for deletion
l.display()