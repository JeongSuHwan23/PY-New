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
    self.front = (self.front + 1) % self.size
    return self.queue[self.front]

  # 가장 처음 들어온 값 출력
  def peek(self):
    if self.isEmpty():
      print("Queue is empty")
      return
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
      print("Data not exist in the queue.")
      return

  def max(self):
    if self.isEmpty():
      print("Queue is empty")
      return

    max_value = self.queue[self.front + 1]
    max_index = self.front + 1

    if self.front < self.rear:
      for i in range(self.front + 2, self.rear + 1):
        if self.queue[i] > max_value:
          max_value = self.queue[i]
          max_index = i
    else:
      for i in range(self.front + 2, self.size):
        if self.queue[i] > max_value:
          max_value = self.queue[i]
          max_index = i
      for i in range(self.rear + 1):
        if self.queue[i] > max_value:
          max_value = self.queue[i]
          max_index = i

    return max_value, max_index


if __name__ == "__main__":
  q = Circular_Queue()
  while True:
    print("1 : enqueue | 2 : dequeue | 3 : peek | 4 : print | 5 : search | 6 : max | 0 : exit")
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
      print("Search data:", end="")
      search_data = int(input())
      result = q.search(search_data)
      if result:
        print("The index of the data is :", result)
      continue
    elif n == 6:
      value, index = q.max()
      if value:
        print("The maximum value is [", value, "] and index is [", index, "]")
      continue
    elif n == 0:
      print("BYE")
      break
    else:
      print("err")
      continue
