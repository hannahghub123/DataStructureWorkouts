class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True
        
    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack empty"
        else:
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        else:
            return self.top.data
        
    def display(self):
        current_node = self.top
        while current_node:
            print(current_node.data,end='->')
            current_node = current_node.next

        print("None")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.display()  # Output: 3 -> 2 -> 1 -> None

print("Peek:", stack.peek())  # Output: Peek: 3

popped_item = stack.pop()
print("Popped:", popped_item)  # Output: Popped: 3

stack.display()  #output: 2->1->None