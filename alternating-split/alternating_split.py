class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    
    head_1 = head
    head_2 = head.next
    tail_1 = head_1
    tail_2 = head_2
    
    i = 0
    cur = head.next.next
    while cur is not None:
        if i%2 == 0:
            tail_1.next = cur
            tail_1 = tail_1.next
        else:
            tail_2.next = cur
            tail_2 = tail_2.next

        cur = cur.next
        i += 1
    
    tail_1.next = None
    tail_2.next = None

    return Context(head_1, head_2)