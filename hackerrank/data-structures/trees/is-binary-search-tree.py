""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(node):
    if node:
        left = right = True
        if node.left and not node.left < node.data:
            left = False
        if node.right and not node.right > node.data:
            right = False

        if left and right:
            return True
        return False

    return check
