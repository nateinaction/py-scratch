class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class MyDict:
    node = None

    def __init__(self):
        """construct a dictionary"""
        pass

    def keytoindex(self, key):
        return int.from_bytes(
            bytearray(key, encoding='utf8'),
            byteorder='big'
        )

    def indextokey(self, index):
        return index.to_bytes(
            (index.bit_length() + 7) // 8,
            byteorder='big', signed=True
        ).decode("utf-8")

    def put(self, key, value, node=None):
        """
        insert an item with key->value into the dictionary
        time complexity: 1
        """
        intkey = self.keytoindex(key)

        if self.node is None:
            self.node = Node(intkey, value)
        elif node is None:
            self.put(key, value, self.node)
        elif node.key > intkey:
            if node.left is None:
                node.left = Node(intkey, value)
            else:
                self.put(key, value, node.left)
        else:
            if node.right is None:
                node.right = Node(intkey, value)
            else:
                self.put(key, value, node.right)

    def get(self, key, node=None):
        """
        get an item with the given key from the dictionary
        time complexity: log(n)
        """
        intkey = self.keytoindex(key)

        if self.node is None:
            return None

        if node is None:
            return self.get(key, self.node)
        elif node.key > intkey:
            return self.get(key, node.left)
        elif node.key < intkey:
            return self.get(key, node.right)

        return self.indextokey(node.key), node.value

    def delete(self, key):
        """
        delete an item with the given key from the dictionary
        time complexity: 1
        """

    def show(self, node):
        if not node:
            return
        self.show(node.left)
        print(self.indextokey(node.key), node.value)
        self.show(node.right)


if __name__ == '__main__':
    mydict = MyDict()
    mydict.put("duck", "quack")
    mydict.put("bear", "roar")
    mydict.put("dog", "woof")
    mydict.show(mydict.node)
    print(mydict.get("bear"))
