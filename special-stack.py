"""
Design a data-structure SpecialStack that supports stack operations like push(), pop() and an
additional operation getMin() which should return minimum element from the SpecialStack.
Your task is to complete all the functions, using stack data-Structure.
"""
from collections import namedtuple

class specialStack:
    stack = []
    min = None

    def push(self, num):
        if not self.stack:
            self.min = key = num
        elif self.min > num:
            key = 2 * num - self.min
            self.min = num
        else:
            key = num

        self.stack.append(key)

        print({'action': 'push', 'input': num, 'min': self.min, 'stack': self.stack})


    def pop(self):
        if not self.stack:
            return None

        item = self.stack.pop()
        if self.min > item:
            self.min = 2 * self.min - item

        print({'action': 'pop', 'min': self.min, 'stack': self.stack})

    def get_min(self):
        print(self.min)


"""
named tuple containing value and current min in the stack.
"""

Item = namedtuple('Item', ['min_so_far', 'elem'])

class specialStack2:
    stack = []

    def push(self, num):
        if not self.stack:
            item = Item(num, num)
        else:
            prev_min = self.stack[-1].min_so_far
            item = Item(num, min(num, prev_min))

        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return None

        return self.stack.pop().elem

    def get_min(self):
        return self.stack[-1].min_so_far


if __name__ == '__main__':
    poke = specialStack2()
    poke.push(10)
    poke.push(5)
    poke.push(6)
    poke.push(1)
    poke.push(0)
    print(poke.stack)
    poke.push(10)
    print(poke.stack)
    poke.pop()
    poke.pop()
    print(poke.stack)
    print(poke.get_min())
