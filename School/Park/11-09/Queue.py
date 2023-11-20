class CircleQueue:
  rear = 0
  front = 0
  MAX_SIZE = 5
  queue = list()

  def __init__(self):
    self.rear = 0
    self.front = 0
    self.queue = [0 for i in range(self.MAX_SIZE)]

  def isEmpty(self):
    if self.rear == self.front:
      return True
    return False

  def isFull(self):
    if (self.rear + 1) % self.MAX_SIZE == self.front:
      return True
    return False

  def enQueue(self, e):
    if self.isFull():
      print("Full")
      return
    self.rear = (self.rear + 1) % self.MAX_SIZE
    self.queue[self.rear] = e

  def deQueue(self):
    if self.isEmpty():
      print("Empty")
      return
    self.front = (self.front + 1) % self.MAX_SIZE
    return self.queue[self.front]

  def peek(self):
    print(self.queue[self.rear])

  def print(self):
    for i in range(self.front, self.rear + 1):
      print(self.queue[i], sep="->")


