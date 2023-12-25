class QueueUsingStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def is_empty(self):
        return not self.enqueue_stack and not self.dequeue_stack
    
    def enqueue(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            raise IndexError("Queue empty")
        return self.dequeue_stack.pop()
    
    def peek(self):
        if not self.dequeue_stack:
            # If the dequeue stack is empty, transfer elements from the enqueue stack
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            raise IndexError("peek from an empty queue")
        return self.dequeue_stack[-1]
        


queue = QueueUsingStack()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())     # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

queue.enqueue(4)
queue.enqueue(5)

print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: 4
print(queue.peek())   #output: 5