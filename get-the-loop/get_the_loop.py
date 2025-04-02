def loop_size(node):
    slow = node.next
    fast = node.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    counter = 1
    slow = slow.next
    while id(slow) != id(fast):
        slow = slow.next
        counter += 1

    return counter
