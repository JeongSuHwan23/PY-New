class Circular_Queue:
  #queue 초기화
  def __init__(self, size=5):
    self.queue = [None] * 5
    self.size = size
    self.front = 0
    self.rear = 0

  #queue 비어있는지 확인
  def isEmpty(self):
    return self.front == self.rear

  #queue 가득 찼는지 확인
  def isFull(self):
    return (self.rear + 1) % self.size == self.front

  #data를 queue에 삽입
  def enqueue(self, data):
    if self.isFull():
      print("Queue is full")
      return

    self.rear = (self.rear + 1) % self.size
    self.queue[self.rear] = data

  #가장 처음 들어온 값 출력 및 제거
  def dequeue(self):
    if self.isEmpty():
      print("Queue is empty")
      return

    self.front = (self.front + 1) % self.size
    print("Dequeue :", self.queue[self.front])

  # 가장 처음 들어온 값 출력 및 제거
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
  q = Circular_Queue()
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