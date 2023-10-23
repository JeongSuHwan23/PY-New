#이상한 출석
n = int(input())
in_list = list(map(int,input().split()))
out_list = list(0 for i in range(23))
t = int(0)
for i in range(0, n) :
    t = in_list[i]
    out_list[t-1] += 1
print(out_list)