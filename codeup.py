#2023-08-16

#6077 짝수 합
n = int(input())
sum = 0
for i in range(2, n+1, +2) :
    sum += i
print(sum)

#6078 q가 입력될 때까지
i = 1
while i==1 :
    c = input()
    print(c)
    if c == 'q' :
        break

#6079
n = int(input())
sum = 0
i = 0
while sum<n : 
    i += 1
    sum += i
print(i)

#6080
a, b = input().split()
n = int(a)
m = int(b)
for i in range(1, n+1) :
    for j in range(1, m+1) :
        print(i, j, sep=' ')

#6081
n = input()
n = int(n, 16)
for i in range(1, 16) :
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

#6082
n = int(input())
for i in range(1, n+1) :
    k = int(i%10)
    if k%3==0 and k!=0:
        print('X', end=' ') 
    else :
        print(i, end=' ')

#6083
r, g, b = map(int, input().split())
count = int(0)
for i in range(r) :
    for j in range(g) :
        for k in range(b) :
            print(i, j, k, sep=' ')
            count += 1
print(count)

#6084
h, b, c, s = map(int, input().split())
m = h*b*c*s/8/1024/1024
print(format(m, ".2f"), 'MB', sep=' ')s-