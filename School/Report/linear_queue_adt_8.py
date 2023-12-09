class Linear_queue:

  # queue 초기화
  def __init__(self, size=5):
    self.queue = [None] * 5
    self.size = size
    self.front = -1
    self.rear = -1

  # queue 비어있는지 확인
  def isEmpty(self):
    return self.front == self.rear

  # queue 가득 찼는지 확인
  def isFull(self):
    return self.rear == self.size - 1

  # data를 queue에 삽입
  def enqueue(self, data):
    if self.isFull():
      print("Queue is full")
      return

    self.rear += 1
    self.queue[self.rear] = data

  # 가장 처음 들어온 값 출력 및 제거
  def dequeue(self):
    if self.isEmpty():
      print("Queue is empty")
      return
    self.front += 1
    return self.queue[self.front]

  # 가장 처음에 들어온 값 출력
  def peek(self):
    if self.isEmpty():
      print("Queue is empty")
      return
    return self.queue[self.front + 1]

  # queue 안에 있는 값 전체 출력
  def print(self):
    if self.isEmpty():
      print("Queue is empty.")
      return

    print_queue = self.queue[self.front + 1: self.rear + 1]

    print("[Front =", self.front, "Rear =", self.rear, "] ==> ", print_queue)

  #입력 받은 값 찾는 함수
  def search(self, data):
    if self.isEmpty():
      print("Queue is empty.")
      return

    for i in range(self.front + 1, self.rear + 1):
      if self.queue[i] == data:
        return i

    print("Data not exist in the queue.")
    return

  #안에 있는 값 다 더하는 함수
  def sum(self):
    if self.isEmpty():
      print("Queue is empty.")
      return

    total = 0
    for i in range(self.front + 1, self.rear + 1):
      total += self.queue[i]

    return total


if __name__ == "__main__":
  q = Linear_queue()
  while True:
    print("1 : enqueue | 2 : dequeue | 3 : peek | 4 : print | 5 : search | 6 : sum | 0 : exit")
    n = int(input())

    if n == 1:
      print("values :", end=" ")
      value = int(input())
      q.enqueue(value)
      continue
    elif n == 2:
      data = q.dequeue()
      if data:
        print("dequeue :", data)
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
      print("Search data :", end=" ")
      search_data = int(input())
      result = q.search(search_data)
      if result:
        print("The index of the data is :", result)
      continue
    elif n == 6:
      total = q.sum()
      if total:
        print("The total sum is [", total, "]")
    elif n == 0:
      print("BYE")
      break
    else:
      print("err")
      continue
