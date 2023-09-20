#서브 스프링
str = input()
a, b = map(int,input().split())
for i in range(a, a+b) :
    print(str[i], end="")

#숫자 피라미드 3
n = int(input())
count = 1
k = 1
a = [[0] * 100 for _ in range(100)]

for i in range(n - 1, -1, -1):
    for j in range(n - k, -1, -1):
        a[i][j] = count
        count += 1
    k += 1

for i in range(n):
    for j in range(i + 1):
        print(a[i][j], end=" ")
    print()

