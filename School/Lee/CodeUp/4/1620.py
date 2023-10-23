def f(k) :
    res = int(0)
    while 1 :
        if k == 0 :
            break
        res += (k%10)
        k //= 10
    return res


n = int(input())
while 1 :
    if (n < 10) :
        break
    n = f(n)
print(n)