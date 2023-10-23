a, d, n = map(int, input().split())
sum = int(a)
for i in range(0, n-1) :
    sum += d
print(sum)