#재귀 (1~n 역순)
def f(k):
    if k == 0:
        return
    print(k)
    f(k - 1)

if __name__ == "__main__":
    n = int(input())
    f(n)