import unittest
from collections import namedtuple

Item = namedtuple('Item', ['char', 'count', 'index_start', 'index_stop'])


def find_longest_substr(s):
    max_item = [Item(None, 0, 0, 0)]
    tracking_char = None
    count = 0
    index_start = 0
    index_stop = 0

    for index, char in enumerate(s):
        char = ord(char)
        if valid_char(char):
            if char is tracking_char:
                count += 1
                index_stop += 1
            else:
                is_max_value(max_item, tracking_char, count, index_start, index_stop)
                tracking_char = char
                count = 1
                index_start = index_stop = index
        else:
            is_max_value(max_item, tracking_char, count, index_start, index_stop)
            tracking_char = None
            count = 0
            index_start = 0
            index_stop = 0

    is_max_value(max_item, tracking_char, count, index_start, index_stop)

    return [max_item[-1].char, max_item[-1].count, [max_item[-1].index_start, max_item[-1].index_stop]]


def is_max_value(max_item, tracking_char, count, index_start, index_stop):
    if count > max_item[-1].count:
        item = Item(str(tracking_char), count, index_start, index_stop)
        max_item.append(item)


def valid_char(ascii_val):
    if 48 <= ascii_val <= 57:
        """0-9"""
        return True
    elif 65 <= ascii_val <= 90:
        """upper case alphabet"""
        return True
    elif 97 <= ascii_val <= 122:
        """lower case alphabet"""
        return True
    return False


class TestStringMethods(unittest.TestCase):
    def test1(self):
        s1 = "1111aa994bbbb1111AAAAAFF?<mmMaaaaaaaaaaaaaaaaaaaaaaaaabf"
        self.assertEqual(find_longest_substr(s1), ['97', 25, [29, 53]])

    def test2(self):
        s2 = "1111aa994bbbb1111AAAAAFF????????????????????????????"
        self.assertEqual(find_longest_substr(s2), ['65', 5, [17, 21]])

    def test3(self):
        s3 = "1111aa994bbbb1111AAAAAFFcfgBBBBB"
        self.assertEqual(find_longest_substr(s3), ['65', 5, [17, 21]])


if __name__ == '__main__':
    print(find_longest_substr("aaa"))
    unittest.main()
