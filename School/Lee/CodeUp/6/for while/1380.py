if __name__ == "__main__":
    n = int(input())
    for i in range(1, n):
        for j in range(n - 1, 0, -1):
            if i > 6:
                break
            if i + j != n or j > 6:
                continue
            else:
                print(i, j)