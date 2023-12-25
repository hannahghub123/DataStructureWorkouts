class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data,end="->")
            current_node = current_node.next

        print("None")


l = Linkedlist()
l.push(1)
l.push(45)
l.push(5)
l.push(10)

l.display()