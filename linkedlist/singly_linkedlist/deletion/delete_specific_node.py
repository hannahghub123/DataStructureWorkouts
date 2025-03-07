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

    def delete_specific_node(self, data):           # func for deleting specific node
        current=self.head                           # set head as current node
        if current and current.data==data:          # check if head data matches
            temp = self.head                        # set head as temporary node
            self.head = temp.next                   # assign next of temp node as head
            del temp                                # delete temp node
            return

        else:
            while current.next.next:                # iterate till next of next node exists
                if current.next.data==data:
                    temp = current.next             # set next node as temporary node
                    current.next=temp.next          # assign next node of temp as the next node
                    del temp                        # delete temp node
                    break
                current=current.next                # move to next node

l = Linkedlist()

l.push(1)                                           # func call for insertion
l.push(45)
l.push(5)
l.push(10)
l.display()                                         # func call for traversal

l.delete_specific_node(5)                           # func call for deletion
l.display()