#기본 입출력
c = input() #입력된 값을 변수(c)에 저장
print(c) #변수(c)를 출력

#입력된 수를 정수로 변환하여 출력
n = input()
n = int(n)
print(n)

#입력된 수를 실수로 변환하여 출력
f = input()
f = float(f)
print(f)

#2개 이상 입력받고 출력
a = input() 
b = input()
a=int(a)
b=int(b)
print(a)
print(b)

#공백을 두고 입력된 정수를 입력받아 출력
a, b = input().split() #spilt() = 공백을 기준으로 자름
a=int(a)
b=int(b)
print(a)
print(b)

#순서를 바꿔서 출력 
a, b = input().split()
print(b, a)

#연속해서 출력
s = input()
print(s, s, s)

#기호를 중심으로 구분하여 입출력
a, b = input().split(':') #':'를 기준으로 자름
print(a, b, sep=':') #':'을 사이에 주고 출력


#2023-07-16

#Y.M.D -> D-M-Y (code up 6019)
y, m, d = input().split('.') #'.'을 기준으로 잘라 순서대로 저장
print(d, m, y, sep='-') #'-'를 사이에 두고 출력

#주민번호입력 (code up 6020)
n, m = input().split('-')
print(n, m, sep='') #(sep = '')을 사용하면 n과 m 사이에 공백없이 출력할 수 있다

#단어 분리해서 출력 (code up 6021)
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
#s[n] = n번째 문자
#ex) Hello의 s[0]='H'

#년도, 월, 일 분리해서 출력 (code up 6022)
s = input()
print(s[0:2], s[2:4], s[4:6], sep=' ')
#s[a,b] = a ~ b-1번째 문자까지 잘라낸 부분
#ex) 123456의 s[0:2] = '12'

#분만 출력 (code up 6023)
h, m, s = input().split(':')
print(m)

#단어 붙여서 출력
w1, w2 = input().split()
print(w1+w2) #w1과 w2를 더해서 공백이 없이 출력 

