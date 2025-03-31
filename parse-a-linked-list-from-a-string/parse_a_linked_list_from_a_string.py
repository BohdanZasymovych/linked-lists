def linked_list_from_string(s):
    if s == 'None':
        return None

    values = s.split(' -> ')
    cur = Node(data=(None if values[0] == 'None' else int(values[0])))
    prev = cur
    head = cur

    for i in values[1:]:
        if i == 'None':
               break
        cur = Node(data=int(i))
        prev.next = cur
        prev = cur

    return head
