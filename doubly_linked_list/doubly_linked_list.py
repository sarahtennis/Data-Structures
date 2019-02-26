"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  # replaces the head of the list with a new value
  # ------- NOTES -------
  # store current head
  # set new head to ListNode(value, None, currentHead)
  # set prevHead.prev to new head
  def add_to_head(self, value):
    # current_head = self.head
    # self.head = ListNode(value, None, current_head)
    # current_head.prev = self.head
    try:
      self.head.insert_before(value)
      self.head = self.head.prev
    except:
      self.tail = ListNode(value)
      self.head = self.tail

    

  # removes the head node and returns the value stored in it
  # ------- NOTES -------
  # store head
  # if head.next, next.prev = None
  # handle if head.next = tail
  # head = storedHead.next
  def remove_from_head(self):
    current_head = self.head

    self.head.delete()

    if current_head.next:
      self.head = current_head.next
    else:
      self.head = None
      self.tail = None
    
    return current_head.value

  # replaces the tail of the list with a new value
  # ------- NOTES -------
  # insert_after on tail, reassign tail
  def add_to_tail(self, value):
    try:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    except:
      self.tail = ListNode(value)
      self.head = self.tail


  # removes the tail node and returns the value stored in it
  # ------- NOTES -------
  # store tail, delete tail, reassign tail
  def remove_from_tail(self):
    current_tail = self.tail
    self.tail.delete()

    if current_tail.prev:
      self.tail = current_tail.prev
    else:
      self.tail = None
      self.head = None
    
    return current_tail.value

  # takes reference to node in list and moves it to front of list, shifting other list nodes down
  # ------- NOTES -------
  # O O O O O O
  # delete referenced node (push together previous neighbors)
  def move_to_front(self, node):
    if node != self.head:
      current_head = self.head

      if self.tail == node and node.prev:
        self.tail = node.prev

      node.delete()
      current_head.prev = node
      node.next = current_head
      self.head = node
    

  # takes reference to node in list and moves it to end of list, shifting other list nodes up
  def move_to_end(self, node):
    if node != self.tail:
      current_tail = self.tail

      if self.head == node and node.next:
        self.head = node.next

      node.delete()
      current_tail.next = node
      node.prev = current_tail
      self.tail = node


  # takes reference to node in list and removes it from the list
  # deleted node's previous and next pointers should point to each afterwards.
  def delete(self, node):
    if self.tail == node:
      if node.prev:
        self.tail = node.prev
      else:
        self.tail = None
    
    if self.head == node:
      if node.next:
        self.head = node.next
      else:
        self.head = None

    node.delete()

    node.next = None
    node.prev = None
  
  # returns the maximum value in the list
  def get_max(self):
    current = self.head
    maximum = 0

    if current.value:
      maximum = self.head.value

      while current.next:
        current = current.next
        maximum = max(maximum, current.value)
    
    return maximum

