# 1,2,3 더하기
num = int(input())
for i in range(num):
  dp = [1, 2, 4]
  n = int(input())
  for j in range(3, n+1):
    dp.append(dp[j-1] + dp[j-2] + dp[j-3])
  print(dp[n-1])