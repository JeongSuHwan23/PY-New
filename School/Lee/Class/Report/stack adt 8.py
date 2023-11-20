class Stack:

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

  def push(self, element):
    if self.isFull():
      print("Full")
      pass
    else:
      self.top += 1
      self.stack.insert(self.top, element)

  def pop(self):
    if self.isEmpty():
      print("Empty")
      pass
    else:
      self.top -= 1
      self.stack.pop()

  def peek(self):
    if self.isEmpty():
      print(self.stack[self.top])
    else:
      pass

  #def print(self):

  #def stackSize(self):

  #def clear:

