"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Reverse(head):
    if not head or not head.next:
        return

    prev_node = None
    node = head
    return _Reverse(prev_node, node)


def _Reverse(prev_node, node):
    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    return prev_node
