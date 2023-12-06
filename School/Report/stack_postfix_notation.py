class ArrayStack:

  # stack 초기화
  def __init__(self, size=5):
    self.stack = [None] * size
    self.size = size
    self.top = -1

  # stack 비어있는지 확인
  def isEmpty(self):
    return self.top == -1

  # stack 가득 차 있는지 확인
  def isFull(self):
    return self.top == self.size - 1

  # 값 삽입
  def push(self, data):
    if self.isFull():
      print("Stack is Full")
    else:
      self.top += 1
      self.stack[self.top] = data

  # 가장 위에 있는 값 출력 and 제거
  def pop(self):
    if self.isEmpty():
      print("Stack is Empty")
    else:
      self.top = self.top - 1
      return self.stack[self.top + 1]

  # 가장 위에 있는 값 출력
  def peek(self):
    if self.isEmpty():
      print("Stack is Empty")
    else:
      return self.stack[self.top]


def precedence(op):
  if op == '*' or op == '/':
    return 2
  elif op == '+' or op == '-':
    return 1
  elif op == '(' or op == ')':
    return 0
  else:
    return -1


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
    elif term in '*/+-':
      while not s.isEmpty():
        op = s.peek()
        if precedence(term) <= precedence(op):
          output.append(op)
          s.pop()
        else:
          break
      s.push(term)
    else:
      output.append(term)
  while not s.isEmpty():
    output.append(s.pop())
  return output


if __name__ == "__main__":
  infix1 = input()
  infix1 = list(infix1)
  postfix = Infix2Postfix(infix1)
  print(postfix)
