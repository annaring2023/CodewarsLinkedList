class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    already_was = set()
    already_was.add(head.data)
    probe = head
    while probe.next is not None:
        data = probe.next.data
        if data in already_was:
            probe.next = probe.next.next
        else:
            already_was.add(probe.next.data)
            probe = probe.next
    return head
