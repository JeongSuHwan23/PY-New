class Stack:

  #스택 초기화 하는 함수
  def __init__(self, size=10):
    self.stack = [None] * 10
    self.size = size
    self.top = -1

  #스택이 비어있는지 확인하는 함수
  def isEmpty(self):
    return self.top == -1

  #스택이 가득 차 있는지 확인하는 함수
  def isFull(self):
    return self.top == self.size - 1

  #값을 삽입하는 함수
  def push(self, element):
    if self.isFull():
      print("Stack is full")
    else:
      self.top += 1
      self.stack[self.top] = element

  #가장 위에 있는 값을 출력하고 제거하는 함수
  def pop(self):
    if self.isEmpty():
      return 0
    else:
      self.top = self.top - 1
      return self.stack[self.top+1]

  #가장 위에 있는 값만 출력하는 함수
  def peek(self):
    if self.isEmpty():
      return 0
    else:
      return self.stack[self.top]

  #스택 출력하는 함수
  def printAll(self):
    if self.isEmpty():
      return 0

    print_stack = self.stack[0 : self.top+1]

    return print_stack

  #모든 값을 더하는 함수
  def valueSum(self):
    if self.isEmpty():
      print("Stack is empty")
      return 0
    else:
      sum = 0
      for i in range (self.top+1):
        sum += self.stack[i]
      return sum

  #스택 초기화 하는 함수
  def clear(self):
    s.top = -1
    print("Stakc cleared")


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
      data = s.pop()
      if not data:
        print("Stack is empty")
      else:
        print("Pop :", data)
      continue
    elif n == 3:
      if not s.peek():
        print("Stack is empty")
      else:
        print("Peek :", s.peek())
      continue
    elif n == 4:
      if not s.valueSum():
        print("Stack is empty")
      else:
        print("Sum result is", s.valueSum())
      continue
    elif n == 5:
      if not s.printAll():
        print("Queue is empty.")
      else:
        print("[ top =", s.top, "] ==>", s.printAll())
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