from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    head.next.next = swap_pairs(head.next.next)

    next_node = head.next
    head.next = next_node.next
    next_node.next = head
