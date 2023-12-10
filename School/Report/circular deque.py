class Deque:
  # 덱 초기화
  def __init__(self, size=5):
    self.size = size
    self.deque = [None] * size
    self.front = 0
    self.rear = 0

  # 덱이 비어있는지 확인
  def isEmpty(self):
    return self.front == self.rear

  # 덱이 가득 차 있는지 확인
  def isFull(self):
    return self.front == (self.rear + 1) % self.size

  # 덱의 앞쪽에 값 추가
  def addFront(self, data):
    if self.isFull():
      print("Deque is full")
      return
    self.front = (self.front - 1) % self.size
    self.deque[self.front] = data

  # 덱의 앞쪽에 있는 값 제거
  def deleteFront(self):
    if self.isEmpty():
      print("Deque is empty")
      return None
    data = self.deque[self.front]
    self.deque[self.front] = None
    self.front = (self.front + 1) % self.size
    return data

  # 덱의 뒤쪽에 값 추가
  def addRear(self, data):
    if self.isFull():
      print("Deque is full")
      return
    self.deque[self.rear] = data
    self.rear = (self.rear + 1) % self.size

  # 덱의 뒤쪽에 있는 값 제거
  def deleteRear(self):
    if self.isEmpty():
      print("Deque is empty")
      return None
    self.rear = (self.rear - 1) % self.size
    data = self.deque[self.rear]
    self.deque[self.rear] = None
    return data

  # 덱의 앞쪽에 있는 값 반환
  def getFront(self):
    if self.isEmpty():
      print("Deque is empty")
      return
    print(self.deque[self.front])
    return self.deque[self.front]

  # 덱의 뒤쪽에 있는 값 반환
  def getRear(self):
    if self.isEmpty():
      print("Deque is empty")
      return
    print(self.deque[(self.rear - 1) % self.size])
    return self.deque[(self.rear - 1) % self.size]


if __name__ == "__main__":
  d = Deque()

  d.addFront(1)
  d.addFront(2)
  d.addRear(3)
  d.addRear(4)
  d.addRear(5)
  print(d.deque)
  d.deleteRear()
  print(d.deque)
  d.deleteFront()
  print(d.deque)
