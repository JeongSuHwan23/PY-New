def f(a):
    if(a==1):
        return 1
    return a * f(a-1)

if __name__=="__main__":
    n = int(input())
    print(f(n))