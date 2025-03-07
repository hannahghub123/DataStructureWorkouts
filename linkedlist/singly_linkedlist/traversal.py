# class for defining node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        # initializing the head as None
        self.head = None

    def traversal(self):
        # assigning the head node as the current node to start with.
        current = self.head

        # if current node exists, the loop runs else it means the list is empty
        while current:
            print(current.data, end=" -> ")
            current = current.next                  # moving to the next node

        print("None")


l = Linkedlist()

l.head = Node(10)  # First node (Head)
l.head.next = Node(20)  # Second node
l.head.next.next = Node(30)   # Third node

# Traverse to check the list
l.traversal()