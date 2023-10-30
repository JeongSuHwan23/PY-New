if __name__ == "__main__":
    a = input().split()
    for i in range(3):
        a[i] = int(a[i])
    a.sort()
    for i in range(3):
        print(a[i],end=" ")

