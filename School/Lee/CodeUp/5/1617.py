
if __name__ == "__main__":
    a = list(input())
    b = []
    sum = int(0)
    n = int(len(a))
    for i in range(n - 1, -1, -1):
        a[i] = int(a[i])
        b.append(a[i])

    for i in range(n):
        sum += (a[i] + b[i]) * (10**i)
    print(sum)
    # if sum // (10 ** (n//2)) == sum % (10 ** (n//2)):
    #     print("YES")
    # else:
    #     print("NO")

