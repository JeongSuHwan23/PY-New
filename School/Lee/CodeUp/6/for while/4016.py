if __name__ == "__main__":
    a, b, c = map(int, input().split())
    while a%b != 0:
        a, b = b, a%b
    while b%c != 0:
        b, c = c, b%c
    print(c)
