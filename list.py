n = int(input())
a = input().split()

for i in range(n) : #0 ~ n-1까지 리스트 생성
    a[i] = int(a[i]) 

d = []
for i in range(24) : 
    d.append(0) #리스트 안에 0을 삽입

for i in range(n) :
    d[a[i]] += 1 

for i in range(1, 24) :
    print(d[i], end=" ")