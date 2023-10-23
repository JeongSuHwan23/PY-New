n = int(input())
list1 = list(map(int,input().split()))
min = list1[0]
for i in range(1, n) :
    if(min>list1[i]) :
        min = list1[i]
print(min)
