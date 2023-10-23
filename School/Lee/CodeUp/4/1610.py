str = input()
a, b = map(int,input().split())
for i in range(a, a+b) :
    print(str[i], end="")
