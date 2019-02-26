class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # adds the input value to the binary search tree
  # ----- NOTES -----
  # check value to see which side to place
  # check if side exists, if so traverse down a level
  # else make new node
  def insert(self, value):
    pointer = self

    while True:
      if value > pointer.value:
        if pointer.right != None:
          pointer = pointer.right
        else:
          pointer.right = BinarySearchTree(value)
          break
      else:
        if pointer.left != None:
          pointer = pointer.left
        else:
          pointer.left = BinarySearchTree(value)
          break

  # return boolean whether value exists in tree
  def contains(self, target):
    pointer = self

    while True:
      if pointer.value == target:
        return True
      elif pointer.value < target and pointer.right != None:
        pointer = pointer.right
      elif pointer.value >= target and pointer.left != None:
        pointer = pointer.left
      else:
        return False

  # returns the maximum value in the binary search tree
  def get_max(self):
    pointer = self

    while True:
      if pointer.right != None:
        pointer = pointer.right
      else:
        return pointer.value
