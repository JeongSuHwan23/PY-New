global s


def reverse(length):
    if length < 0:
        return
    print(s[length], end="")
    reverse(length - 1)


if __name__ == "__main__":
    s = input()
    s_length = len(s)
    reverse(s_length - 1)
