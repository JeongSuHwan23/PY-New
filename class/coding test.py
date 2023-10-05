def sum(list_2, index) :
    if index < 0 :
        return 0
    else :
        return list_2[index] + sum(list_2, index-1)

if __name__ == "__main__":
    list_1 = input().split()

    list_1 =  [int(x) for x in list_1]

    result = sum(list_1, len(list_1)-1)
    print(result)

def pop(sum):
    global myList
    if myList:
        pop(sum+myList.pop())
    else:
        print(sum)
        return

if __name__ == "__main__":
    myList = input().split()
    myList = [int(x) for x in myList]
    pop(0)

