#재귀 (1~n)
def p(n):
    if n < 1:
        return
    p(n - 1)
    print(n)

if __name__ == "__main__":
    m = int(input())
    p(m)
