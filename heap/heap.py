'''
heap is complete binary tree ---> every level must be filled, except last
can represent with list since complete
min-heap: value of each node >= to the value of its parent, with the minimum-value element at the root.
max-heap: value of each node <= the value of its parent, with the maximum-value element at the root.

    10
   /  \
  4    5    --->  [10, 4, 5, 3, 2, 1]
 / \    \
3   2    1

parent 0 --> child 1, child 2
parent 1 --> child 3, child 4
parent 2 --> child 5
'''

import math

# MAX HEAP
class Heap:
  def __init__(self):
    self.storage = []

  # adds the input value into the correct position in heap
  def insert(self, value):
    # add value to storage, O(1)
    self.storage.append(value)

    # move new value to correct position, O(n) if value is new max
    self._bubble_up(self.get_size() - 1)

  # removes and returns the 'topmost' value from the heap (maintain max heap property)
  def delete(self):
    if self.get_size() == 0:
      return
    elif self.get_size() == 1:
      return self.storage.pop()
    
    # has 2+ elements
    max_parent = self.storage[0]
    self.storage[0] = self.storage.pop()
    self._sift_down(0)

    return max_parent
    
  # returns the maximum value in the heap in constant time
  def get_max(self):
    return self.storage[0]

  # returns number of values in heap
  def get_size(self):
    return len(self.storage)

  # moves element at index "up" the heap
  # swapping it with parent, if parent value < value at index
  def _bubble_up(self, index):
    parent_index = math.floor((index - 1) / 2)
    
    if parent_index < 0:
      return
    
    if self.storage[parent_index] < self.storage[index]:
      temp = self.storage[parent_index]
      self.storage[parent_index] = self.storage[index]
      self.storage[index] = temp

      self._bubble_up(parent_index)
      

  # grabs indices of element's children and determines which child has larger value
  # If larger child's value > parent's value, swap child with the parent
  def _sift_down(self, index):
    left = index * 2 + 1
    right = index * 2 + 2
    
    if right < self.get_size():
      if self.storage[left] > self.storage[right]:
        max_index = left
      else:
        max_index = right
    elif left < self.get_size():
      max_index = left
    else:
      return

    if self.storage[index] < self.storage[max_index]:
      temp = self.storage[index]
      self.storage[index] = self.storage[max_index]
      self.storage[max_index] = temp

      self._sift_down(max_index)
      

    
