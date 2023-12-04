class Queue:
  def __init__(self, size=5):
    self.queue = [None] * 5
    self.size = size
    self.front = 0
    self.rear = 0

  def isEmpty(self):
    return self.front == self.rear

  def isFull(self):
    return (self.rear + 1) % self.size == self.front

  def enqueue(self, data):
    if self.isFull():
      print("Queue is full")
      return

    self.rear = (self.rear + 1) % self.size
    self.queue[self.rear] = data

  def dequeue(self):
    if self.isEmpty():
      print("Queue is empty")
      return

    self.front = (self.front + 1) % self.size
    print("Dequeue :", self.queue[self.front])

  def peek(self):
    if self.isEmpty():
      print("Queue is empty")
      return

    print("Peek :", self.queue[self.front])

  def print(self):
    if self.isEmpty():
      print("Queue is empty.")
      return

    if self.front < self.rear:
      print_queue = self.queue[self.front + 1: self.rear + 1]
    else:
      print_queue = self.queue[self.front + 1: self.size] + self.queue[0: self.rear + 1]

    print("[Front =", self.front, "Rear =", self.rear, "] ==> ", print_queue)


if __name__ == "__main__":
  q = Queue()
  while True:
    print("1 : enqueue | 2 : dequeue | 3 : peek | 4 : print | 0 : exit")
    n = int(input())

    if n == 1:
      print("values :", end=" ")
      value = int(input())
      q.enqueue(value)
      continue
    elif n == 2:
      q.dequeue()
      continue
    elif n == 3:
      q.peek()
      continue
    elif n == 4:
      q.print()
      continue
    elif n == 0:
      print("BYE")
      break
    else:
      print("err")
      continue