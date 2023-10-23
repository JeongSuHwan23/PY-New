n = int(input())

d = input().split()

for i in range(n) :
    d[i] = int(d[i])
    d.append(d[i])

rank = []
for i in range(n) :
    temp = 1
    for j in range(i, n+i) :
            if d[i] < d[j] :
                temp+=1
    rank.append(temp)

for i in range (n) :
    print(d[i], rank[i], end=" ")
    print()
