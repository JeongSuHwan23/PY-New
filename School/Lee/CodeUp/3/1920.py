def f(a):
    if a>1:
        f(a//2)
    print(a%2, end="")

if __name__=="__main__":
    n = int(input())
    f(n)