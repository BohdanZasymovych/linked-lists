""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head is None:
        new_head = Node(data)
        return new_head

    if data < head.data:
        new_head = Node(data)
        new_head.next = head
        return new_head

    cur = head
    prev = None
    while cur is not None and data > cur.data:
        prev = cur
        cur = cur.next

    new_node = Node(data)
    prev.next = new_node
    new_node.next = cur
