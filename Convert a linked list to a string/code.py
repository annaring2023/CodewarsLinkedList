from node import Node
def stringify(node):
    if node:
        listic = []
        probe = node
        while probe is not None:
            listic.append(str(probe.data))
            probe = probe.next

        listic.append("None")
        return " -> ".join(listic)
    return "None"
