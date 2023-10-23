def f(n, m):
    if n>m:
        return
    if n%2!=0:
        print(n)
    f(n+1, m)

if __name__=="__main__":
    a, b = map(int, input().split())
    f(a, b)