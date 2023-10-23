a, m, d, n = map(int, input().split())
result = int(a)
for i in range(0, n-1) :
    result = result*m+d
print(result)