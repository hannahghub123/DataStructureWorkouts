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

    def delete_at_start(self):
        if self.head is None:                       # check if list is empty
            return
        else:
            temp = self.head                        # set head as temporary node
            self.head=temp.next                     # assign next node of head as head

            del temp                                # delete the temporary node


l = Linkedlist()
l.push(1)                                           # func call for insertion
l.push(45)
l.push(5)
l.push(10)
l.display()                                         # func call for traversal

l.delete_at_start()                                 # func call for deletion
l.display()