from node import Node
def sorted_insert(head, data):
    if head is None:
        return Node(data)
    if head.data > data:
        new = Node(data)
        new.next = head
        head = new
        return head
    probe = head
    while probe.next and probe.next.data < data:
        probe = probe.next
    new_node = Node(data)
    new_node.next = probe.next
    probe.next = new_node
    return head
