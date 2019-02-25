class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  # add an item to the back of the queue
  def enqueue(self, item):
    self.storage.append(item)
    self.size += 1
  
  # remove and return an item from the front of the queue
  def dequeue(self):
    if self.len():
      front = self.storage[0]
      del self.storage[0]

      self.size -= 1

      return front

  #returns the number of items in the queue
  def len(self):
    return self.size
