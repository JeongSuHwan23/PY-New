
if __name__ == "__main__":
    a = list(input())
    b = []
    sum = int(0)
    for i in range(len(a) - 1, -1, -1):
        a[i] = int(a[i])
        b.append(a[i])

    for i in range(len(a)):
        sum += (a[i] + b[i]) * (10**i)
    print(a, b, sum)

