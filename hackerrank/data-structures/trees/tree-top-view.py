class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def topView(node, data=[]):
    if node:
        if node.left:
            data = go_left(node.left, data)
        data.append(node.data)
        if node.right:
            data = go_right(node.right, data)

    print(" ".join(str(i) for i in data))


def go_left(node, data=[]):
    if node:
        data.insert(0, node.data)
        return go_left(node.left, data)
    return data


def go_right(node, data=[]):
    if node:
        data.append(node.data)
        return go_right(node.right, data)
    return data


if __name__ == '__main__':
    input1 = [47, 2, 40, 20, 38, 30, 14, 28, 10, 16, 19, 44, 39, 27, 7, 9, 31, 12, 43, 21, 5, 41, 34, 49, 13, 33, 3, 4,
             25, 22, 29, 15, 32, 35, 6, 24, 23, 26, 1, 11, 42, 36, 37, 17, 18, 8, 45, 48, 50, 46]
    expect = [1, 2, 47, 49, 50]

    tree = BinarySearchTree()
    for n in input1:
        tree.create(n)
    print("actual:")
    topView(tree.root)
    print("expected:", expect)
