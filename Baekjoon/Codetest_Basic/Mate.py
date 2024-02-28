#최대공약수와 최소공배수
def GCD(x, y):
  while(y):
    x, y = y, x%y
  return x

def LCM(a, b, c):
  return (a * b) // c

n, m = map(int,input().split())
t = (GCD(n, m))
print(t)
print(LCM(n, m, t))

#소수 찾기
import math

def Prime(k):
  if k < 2 :
    return False
  for i in range(2, int(math.sqrt(k)) + 1):
    if(k%i == 0):
      return False
  return True

cnt = 0
n = int(input())
f = list(map(int,input().split()))
for i in range(n):
  if Prime(f[i]):
    cnt += 1
print(cnt)

#소수 구하기
import math

def Prime(k):
  if k < 2 :
    return
  for i in range(2, int(math.sqrt(k)) + 1):
    if(k%i == 0):
      return
  print(k)  

m, n = map(int,input().split())
f = list()
for i in range(m, n+1):
  Prime(i)

