n = int(input())
seq_list = list(map(int,input().split()))
for i in range (1, n+1) :
    print(seq_list[n-i],end=" ")
