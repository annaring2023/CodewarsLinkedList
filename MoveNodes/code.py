class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise IndexError()
    moving_first = source
    source = source.next
    moving_first.next = dest
    dest = moving_first
    return Context(source, dest)
