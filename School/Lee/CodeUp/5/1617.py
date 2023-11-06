def reverse(num):
    reserve_n = int(str(num)[::-1])

    result = reserve_n + num

    return str(result) == str(result)[::-1]


if __name__ == "__main__":
    n = int(input())

    if reverse(n):
        print("YES")
    else:
        print("NO")

