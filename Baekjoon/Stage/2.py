#1330 두 수 비교하기
n, m = map(int,input().split())
if (n>m): print(">")
elif (n<m): print("<")
else: print("==")

#9498 시험 성적
score = int(input())
if (score >= 90): print("A")
elif (score >= 80): print("B")
elif (score >= 70): print("C")
elif (score >= 60): print("D")
else: print("F")

#2753 윤년
year = int(input())
if((year%4==0 and year%100 != 0) or year%400==0): print("1")
else: print(0)

#2480 주사위 3개
a, b, c = map(int,input().split())
if(a==b==c): print(10000+(a*1000))
elif (a==b): print(1000+(a*100))
elif (b==c): print(1000+(b*100))
elif (c==a): print(1001000+(c*100))
else:
  if(a>b and a>c): print(a*100)
  elif(b>c and b>a): print(b*100)
  else: print(c*100)