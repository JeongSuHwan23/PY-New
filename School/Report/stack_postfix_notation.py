class ArrayStack:

  # 스택 초기화 하는 함수
  def __init__(self, capacity):
    self.stack = [None] * 100
    self.capacity = 100
    self.top = -1

  # 스택이 비어있는지 확인하는 함수
  def isEmpty(self):
    return self.top == -1

  # 스택이 가득 차 있는지 확인하는 함수
  def isFull(self):
    return self.top == self.capacity - 1

  # 값을 삽입하는 함수
  def push(self, element):
    if self.isFull():
      print("Stack is full")
      return
    self.top += 1
    self.stack.insert(self.top, element)

  # 가장 위에 있는 값을 출력하고 제거하는 함수
  def pop(self):
    if self.isEmpty():
      print("Stack is empty")
      pass
    else:
      print("pop :", self.stack[self.top])
      return self.stack[self.top]
      self.top -= 1

  # 가장 위에 있는 값만 출력하는 함수
  def peek(self):
    if self.isEmpty():
      print("Stack is empty")
      pass
    else:
      print("peek :", self.stack[self.top])


def precedence(op):
  if op == '*' or op == '/':
    return 2
  elif op == '+' or op == '-':
    return 1
  elif op == '(' or op == ')':
    return 0
  else:
    return - 1


def Infix2Postfix(expr):
  s = ArrayStack(100)
  output = []

  for term in expr:
    if term in '(':
      s.push('(')

    elif term in ')':
      while not s.isEmpty():
        op = s.pop()
        if op == '(':
          break
        else:
          output.append(op)

    elif term in "*/+-":
      while not s.isEmpty():
        op = s.peek()
        if precedence(term) <= precedence(op):
          output.append(op)
          s.pop
        else:
          break
      s.push(term)

    else:
      output.append(term)

  while not s.isEmpty():
    output.append(s.pop())

  return output
