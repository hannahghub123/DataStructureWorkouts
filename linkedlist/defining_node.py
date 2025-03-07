# defining a node

'''
A node has two important parts - 
1. data - which holds the value of the node
2. next pointer - which holds the reference to the next node
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None