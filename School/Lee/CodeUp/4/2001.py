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
