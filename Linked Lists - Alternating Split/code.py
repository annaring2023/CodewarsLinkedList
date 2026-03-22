class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise IndexError()
    head1 = head
    head2 = head.next
    curr_head1 = head1
    curr_head2 = head2
    head_curr = head.next.next
    while head_curr:
        curr_head1.next = head_curr
        curr_head1 = head_curr
        head_curr = head_curr.next
        if head_curr:

            curr_head2.next = head_curr
            curr_head2 = head_curr
            head_curr = head_curr.next
        else:
            curr_head2.next = None
            break
    curr_head1.next = None
    if curr_head2:
        curr_head2.next = None
    return Context(head1, head2)
