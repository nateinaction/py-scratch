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
        if self.root is None:
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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def height(node):
    if node:
        return 1 + max(height(node.left), height(node.right))
    else:
        return -1


"""
tree = BinarySearchTree()
t = int(input())

for _ in range(t):
    x = int(input())
    tree.create(x)

print(height(tree.root))
"""

if __name__ == '__main__':
    tree1 = BinarySearchTree()
    input1 = [7, 3, 5, 2, 1, 4, 6, 7]
    for n in input1:
        tree1.create(n)
    print("actual:", height(tree1.root), "expected: 3")

    input2 = [15, 1, 3, 2, 5, 4, 6, 7, 9, 8, 11, 13, 12, 10, 15, 14]
    tree2 = BinarySearchTree()
    for n in input2:
        tree2.create(n)
    print("actual:", height(tree2.root), "expected: 9")
