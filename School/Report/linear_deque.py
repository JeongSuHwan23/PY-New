class Linear_deque:

  # queue 초기화
  def __init__(self, size=5):
    self.deque = [None] * 5
    self.size = size
    self.front = -1
    self.rear = -1

  # queue 비어있는지 확인
  def isEmpty(self):
    return self.front == self.rear

  # queue 가득 찼는지 확인
  def isFull(self):
    return self.rear == self.size - 1

  def add_front(self, data):


  def add_rear(self, data):
    if self.isFull():
      print("Deque is full")
      return

    self.rear += 1
    self.queue[self.rear] = data

  def delete_front(self):
    if self.isEmpty():
      print("Queue is empty")
      return
    self.front += 1
    return self.queue[self.front]

  def delete_rear(self):

  def peek(self):
    if self.isEmpty():
      print("Queue is empty")
      return
    return self.queue[self.front + 1]