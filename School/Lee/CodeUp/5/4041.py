if __name__ == "__main__":
    n = int(input())
    n_reverse = int(0)
    n_sum = int(0)
    while n != 0:
        k = int(n % 10)
        if k != 0:
            n_reverse += k * ((10 ** len(str(n))) // 10)
        n_sum += k
        n //= 10
    print(n_reverse)
    print(n_sum)
