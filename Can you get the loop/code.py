from node import Node
def loop_size(node):
    slow = node
    fast = node
    count = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            point = slow
            while fast.next != point:
                count += 1
                fast = fast.next
            return count + 1
