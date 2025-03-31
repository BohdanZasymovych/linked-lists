def stringify(node):
    values = []
    cur = node
    while cur is not None:
        values.append(cur.data)
        cur = cur.next
    values.append(None)

    return ' -> '.join(map(str, values))
