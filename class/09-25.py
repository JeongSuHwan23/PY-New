#서브 스트링
str = input()
a, b = map(int,input().split())
for i in range(a, a+b) :
    print(str[i], end="")

#숫자 피라미드
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

    
#자릿수의 합
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


#최소 대금
a = list()
b = list()
for i in range (0, 3) :
    n = int(input())
    a.append(n)
for j in range (2) :
    m = int(input())
    b.append(m)
a.sort()
b.sort()
result = float(a[0]+b[0])
result += result/10
print(result)

#자릿수 계산
n = int(input())
print(len(str(n)))

#별 계단
n = int(input())
for i in range (n) :
    for j in range (i) :
        print(end=' ')
    print("**")




