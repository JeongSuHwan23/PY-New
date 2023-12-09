class Deque:
  def __init__(self, size=5):
    self.deque = [None] * size
    self.front = -1
    self.rear = -1
    self.size = size

  def isEmpty(self):
    return self.front == -1

  def isFull(self):
    return self.front == 0 and self.rear == self.size - 1

  def addFront(self, item):
    if self.isFull():
      print("Deque is full")
      return
    if self.isEmpty():
      self.front = self.rear = 0
    else:
      self.front -= 1
      if self.front < 0:
        self.front = self.size - 1
    self.deque[self.front] = item

  def addRear(self, item):
    if self.isFull():
      print("Deque is full")
      return
    if self.isEmpty():
      self.front = self.rear = 0
    else:
      self.rear += 1
      if self.rear == self.size:
        self.rear = 0
    self.deque[self.rear] = item

  def deleteFront(self):
    if self.isEmpty():
      print("Deque is empty")
      return None
    item = self.deque[self.front]
    self.deque[self.front] = None
    if self.front == self.rear:
      self.front = self.rear = -1
    else:
      self.front += 1
      if self.front == self.size:
        self.front = 0
    return item

  def deleteRear(self):
    if self.isEmpty():
      print("Deque is empty")
      return None
    item = self.deque[self.rear]
    self.deque[self.rear] = None
    if self.front == self.rear:
      self.front = self.rear = -1
    else:
      self.rear -= 1
      if self.rear < 0:
        self.rear = self.size - 1
    return item

  def getFront(self):
    if self.isEmpty():
      print("Deque is empty")
      return None
    return self.deque[self.front]

  def getRear(self):
    if self.isEmpty():
      print("Deque is empty")
      return None
    return self.deque[self.rear]

