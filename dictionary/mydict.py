class MyDict:
    dict = []*max(i)

    def __init__(self):
        """construct a dictionary"""
        pass

    def keytoindex(self, key):
        return int.from_bytes(
            bytearray(key, encoding='utf8'),
            byteorder='big'
        )

    def put(self, key, value):
        """
        insert an item with key->value into the dictionary
        time complexity: 1
        """
        intkey = self.keytoindex(key)
        self.dict[intkey] = value

    def get(self, key):
        """
        get an item with the given key from the dictionary
        time complexity: 1
        """
        intkey = self.keytoindex(key)
        return self.dict[intkey]

    def delete(self, key):
        """
        delete an item with the given key from the dictionary
        time complexity: 1
        """
        intkey = self.keytoindex(key)
        del self.dict[intkey]
        return None

    def show(self):
        return self.dict


if __name__ == '__main__':
    dict = MyDict()
    dict.put("poke", 12345)
    dict.put(1, "blah")
    print(dict.show())
    print()


# int key to bytes
# key.to_bytes((key.bit_length() + 7) // 8, byteorder='big', signed=True)
