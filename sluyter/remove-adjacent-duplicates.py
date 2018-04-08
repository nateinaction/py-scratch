"""
[2:07 PM] Michael Sluyter: remove duplicates -- given a string, remove *adjacent* duplicates. so for example
[2:08 PM] Michael Sluyter:
    "1aaaaaa2aaaaaa3bbb4444q"
[2:08 PM] Michael Sluyter: output would be:
[2:08 PM] Michael Sluyter:
    1a2a3b4q
"""

import unittest


def remove_adjacent_duplicates(string):
    return "".join([string[0]] + [string[i] for i in range(1, len(string)) if string[i - 1] != string[i]])


class TestMe(unittest.TestCase):
    def test_1(self):
        string = "1aaaaaa2aaaaaa3bbb4444q"
        expect = "1a2a3b4q"
        self.assertEqual(remove_adjacent_duplicates(string), expect)


if __name__ == '__main__':
    unittest.main()
