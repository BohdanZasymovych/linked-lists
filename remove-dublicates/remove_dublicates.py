class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None

    cur = head.next
    prev = head
    while cur is not None:
        if prev.data == cur.data:
            prev.next = cur.next
            cur = cur.next
            continue

        prev = cur
        cur = cur.next

    return head
