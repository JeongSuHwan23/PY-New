def pop(sum):
    global myList
    if myList:
        pop(sum*myList.pop())
    else:
        print(sum)
        return

if __name__ == "__main__":
    myList = input().split()
    myList = [int(x) for x in myList]
    pop(1)