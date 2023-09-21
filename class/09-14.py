a = [[0]*19 for _ in range(19)]

n = int(input())

for i in range (n) :
    x, y = input().split()
    a[int(x)-1][int(y)-1] = 1

for i in range (19) :
    print(*a[i])