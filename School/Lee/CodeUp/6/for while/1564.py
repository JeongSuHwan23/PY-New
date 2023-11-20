if __name__ == "__main__":
    a, b = map(int, input().split())
    while a%b != 0:
        a, b = b, a%b
    print(b)