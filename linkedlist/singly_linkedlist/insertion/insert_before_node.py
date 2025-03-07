class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    # func to insert node to the end
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head                    # create a new node
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node                # Link end node to new node

    # func to insert node before a specified node
    def push_before_node(self, data, key):
        new_node = Node(data)                           # create new node

        # Case 1: If list is empty
        if self.head is None:
            print("List is empty")
            return
        
        # Case 2: If key is at the head
        if self.head.data == key:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Case 3: Traverse to find key node
        current = self.head
        while current.next:
            if current.next.data == key:
                new_node.next = current.next            # Point new node to key node
                current.next = new_node                 # Link previous node to new node
                return
            
            current = current.next

        print(f"Key {key} not found in the list")

    # func for list traversal
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next

        print("None")


l = LinkedList()

l.push(1)
l.push(45)
l.push(5)
l.push(10)
l.display()

l.push_before_node(35,45)
l.display()

