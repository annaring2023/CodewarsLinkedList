from node import Node
def get_nth(node, index):
    head = node
    probe = head
    count = 0
    if index < 0:
        raise IndexError()
    if node is None:
        raise IndexError()
    while probe:
        if count == index:
            return probe
        probe = probe.next
        count += 1
    raise IndexError()
