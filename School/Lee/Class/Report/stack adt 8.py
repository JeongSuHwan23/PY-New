class Stack:

  #스택 초기화 하는 함수
  def __init__(self):
    self.stack = []
    self.size = 3
    self.top = -1

  #스택이 비어있는지 확인하는 함수
  def isEmpty(self):
    return self.top == -1

  #스택이 가득 차 있는지 확인하는 함수
  def isFull(self):
    return self.top == self.size-1

  #값을 삽입하는 함수
  def push(self, element):
    if self.isFull():
      print("Full")
      pass
    else:
      self.top += 1
      self.stack.insert(self.top, element)

  #가장 위에 있는 값을 출력하고 제거하는 함수
  def pop(self):
    if self.isEmpty():
      print("Empty")
      pass
    else:
      print("pop :", self.stack[self.top])
      self.top -= 1

  #가장 위에 있는 값만 출력하는 함수
  def peek(self):
    if self.isEmpty():
      print("Empty")
      pass
    else:
      print("peek :", self.stack[self.top])

  #스택 전체를 출력하는 함수
  def printAll(self):
    for i in range(self.top+1):
      print(self.stack[i], end="->")
    print()

  #모든 값을 출력하는 함수
  def valueSum(self):
    sum = 0
    for i in range (self.top+1):
      sum += self.stack[i]
    print("Sum result is", sum)

  #스택 초기화 하는 함수
  def clear(self):
    s.top = -1
    print("Clear")


if __name__ == "__main__":
  s = Stack()
  while True:
    print("1 : push | 2 : pop | 3 : peek | 4 : sum | 5 : print | 6 : clear | 0 : exit")
    n = int(input())

    if n == 1:
      print("values :", end=" ")
      value = int(input())
      s.push(value)
      continue
    elif n == 2:
      s.pop()
      continue
    elif n == 3:
      s.peek()
      continue
    elif n == 4:
      s.valueSum()
      continue
    elif n == 5:
      s.printAll()
      continue
    elif n == 6:
      s.clear()
      continue
    elif n == 0:
      print("BYE")
      break
    else:
      print("err")
      continue