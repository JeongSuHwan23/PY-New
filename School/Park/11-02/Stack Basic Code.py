stack_size = 5
list = []
top = -1


def isEmpty():
    if top == -1:
        return True
    else:
        return False


def isFull():
    if top == stack_size - 1:
        return True
    else:
        return False


def push(e):
    global top
    if isFull() == 1:
        print("Full")
        exit()
    else:
        top += 1
        list.insert(top, e)
        print(list)


def pop():
    global top
    if isEmpty() == 1:
        print("Empty")
        exit()
    else:
        top -= 1
        list.pop()
        print(list)


def peek():
    if not isEmpty():
        return list[top]
    else:
        pass


if __name__ == "__main__":
    push(1)
    push(2)
    push(1)
    push(2)
    push(1)
    push(2)
    push(1)
    push(2)
