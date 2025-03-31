from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    if head is None:
        return Node(data)

    node = Node(data)
    node.next = head

    return node

def build_one_two_three():
    head = push(None, 3)
    head = push(head, 2)
    head = push(head, 1)
