class MyDict:
    keys = []
    values = []

    def __init__(self):
        """construct a dictionary"""
        pass

    def put(self, key, value):
        """
        insert an item with key->value into the dictionary
        time complexity: 1
        """
        self.keys.append(key)
        self.values.append(value)

    def get(self, key):
        """
        get an item with the given key from the dictionary
        time complexity: n, ugh
        """
        index = self.keys.index(key)
        return self.values[index]

    def delete(self, key):
        """
        delete an item with the given key from the dictionary
        time complexity: 1
        """
        index = self.keys.index(key)
        del self.keys[index]
        del self.values[index]
        return None

    def show(self):
        return list(zip(self.keys, self.values))


if __name__ == '__main__':
    meow = MyDict()
    meow.put("poke", 12345)
    meow.put(1, "blah")
    meow.put("quack", "duck")
    print(meow.show())
    print(meow.get("poke"))
    print(meow.delete("quack"))
    print(meow.show())
    #print(meow.get("ayay"))


# int key to bytes
# key.to_bytes((key.bit_length() + 7) // 8, byteorder='big', signed=True)
