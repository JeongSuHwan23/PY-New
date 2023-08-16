#2023-08-16

#무한 출력
n = 1
while n!=0 : 
    n = int(input())
    if n!=0 :
        print(n)

#카운트다운
n = int(input())
while n>0 :
    print(n)
    n -= 1

#알파벳 출력
c = ord(input())
t = ord('a')
while t<=c :
    print(chr(t), end=' ')
    t += 1

#0부터 N까지 출력 (while)
n = int(input())
i = int(0)
while i<=n :
    print(i)
    i += 1

#0부터 N까지 출력 (for)
n = int(input())
for i in range(n+1) :
  print(i)

#range(n) => 0 ~ n-1
#range(끝)
#range(시작, 끝)
#range(시작, 끝, 증감)