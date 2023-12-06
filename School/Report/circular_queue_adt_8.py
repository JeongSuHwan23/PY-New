class Circular_Queue:

  # queue 초기화
  def __init__(self, size=5):
    self.queue = [None] * 5
    self.size = size
    self.front = 0
    self.rear = 0

  # queue 비어있는지 확인
  def isEmpty(self):
    return self.front == self.rear

  # queue 가득 찼는지 확인
  def isFull(self):
    return (self.rear + 1) % self.size == self.front

  # data를 queue에 삽입
  def enqueue(self, data):
    if self.isFull():
      print("Queue is full")
      return

    self.rear = (self.rear + 1) % self.size
    self.queue[self.rear] = data

  # 가장 처음 들어온 값 출력 및 제거
  def dequeue(self):
    if self.isEmpty():
      print("Queue is empty")
      return
    else:
      self.front = (self.front + 1) % self.size
      return self.queue[self.front]

  # 가장 처음 들어온 값 출력
  def peek(self):
    if self.isEmpty():
      print("Queue is empty")
      return
    else:
      return self.queue[self.front]

  # queue 안에 있는 값 전체 출력
  def print(self):
    if self.isEmpty():
      print("Queue is empty.")
      return

    if self.front < self.rear:
      print_queue = self.queue[self.front + 1: self.rear + 1]
    else:
      print_queue = self.queue[self.front + 1: self.size] + self.queue[0: self.rear + 1]

    print("[Front =", self.front, "Rear =", self.rear, "] ==> ", print_queue)

  # queue 안에서 data 위치 탐색
  def search(self, data):
    if self.isEmpty():
      print("Queue is empty.")
      return

    if self.front < self.rear:
      search_queue = self.queue[self.front + 1: self.rear + 1]
    else:
      search_queue = self.queue[self.front + 1: self.size] + self.queue[0: self.rear + 1]

    try:
      index = search_queue.index(data)
      return (self.front + 1 + index) % self.size
    except ValueError:
      print("Value not exist in the queue.")
      return


if __name__ == "__main__":
  q = Circular_Queue()
  while True:
    print("1 : enqueue | 2 : dequeue | 3 : peek | 4 : print | 5 : search | 0 : exit")
    n = int(input())

    if n == 1:
      print("values :", end=" ")
      value = int(input())
      q.enqueue(value)
      continue
    elif n == 2:
      data = q.dequeue()
      if data:
        print("Dequeue :", data)
      continue
    elif n == 3:
      peek_data = q.peek()
      if peek_data:
        print("Peek :", peek_data)
      continue
    elif n == 4:
      q.print()
      continue
    elif n == 5:
      print("Data to search1 :", end="")
      data = int(input())
      data_location = q.search(data)
      if data_location:
        print("The location of the data is :", data_location)
      continue
    elif n == 0:
      print("BYE")
      break
    else:
      print("err")
      continue
