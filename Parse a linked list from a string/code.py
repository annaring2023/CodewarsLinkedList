from node import Node
def linked_list_from_string(list_repr: str) -> Node | None:
    if not list_repr:
        return None
    new_list = list(list_repr.split(" -> "))
    if new_list[-1] == "None":
        new_list.pop()
    head = None
    for el in reversed(new_list):
        head = Node(int(el), head)
    return head
