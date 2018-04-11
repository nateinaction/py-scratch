class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def tree_height(node):
    pass


def _tree_height(node):
    if not node:
        return -1

    return max(1 + _tree_height(node.left), 1 + _tree_height(node.right))


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.create(5)
    tree.create(7)

    print(tree)
    print(_tree_height(tree.root) - 1)
