class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    if not head:
        return

    hashes_dict = {}
    node = head
    while node:
        if node.next in hashes_dict:
            return True
        hashes_dict[node.next] = 1
        node = node.next
    return False


def has_cycle_with_id(head):
    if not head:
        return

    hashes_dict = {}
    node = head
    while node:
        if id(node.next) in hashes_dict:
            return True
        hashes_dict[id(node.next)] = 1
        node = node.next
    return False


if __name__ == '__main__':
    poke = Node()
    poke2 = Node()
    poke.data = 1
    poke2.data = 2
    poke.next = poke2
    # poke2.next = poke
    print(has_cycle(poke))



