#2023-07-17

#arithmetic operation(산술 연산)

#부호바꾸기
n = int(input())
print(-n) #변수 앞에 '-'를 붙이면 부호가 반대인 값이 된다

#다음 문자 출력
c = ord(input()) #문자를 정수 값으로 입력 받는다
print(chr(c+1)) #정수에 1을 더한 값을 문자로 바꿔서 출력한다

#차 계산
a, b = input().split()
c = int(a) - int(b) 
print(c)

#곱 계산
a, b = input().split()
c = float(a) * float(b)
print(c)

#단어 여러 번 출력
w, n = input().split()
print(w*int(n)) #(문자) * (정수)를 하면 정수만큼 문자를 출력한다

#거듭제곱 계산
a, b = input().split()
c = int(a)**int(b) # a**b = a를 b번 제곱한다
print(c)

#몫 계산
a, b = input().split()
print(int(a)//int(b)) #'//'는 몫이 정수형(int)으로 나온다

#나머지 계산
a, b = input().split()
print(int(a)%int(b))

#자동 계산
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
c = float(a)/float(b) #'/'는 몫이 실수형(float)으로 나온다
print(format(c, ".2f"))

#합, 평균 계산
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a+b+c
avg = float(a+b+c)/3
print(sum, format(avg, ".2f"))

#2023-07-20

#bitwise operators (비트쉬프트연산)

#2배 출력
n = int(input())
print(n<<1) # 'N<<1' = N*2 // 'N>>1' = N * 1/2

#거듭제곱
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b) # a<<b = a*(2**b)

#-------------------------------------
#comparative operation(비교연산)

#정수 2개 비교
a, b = input().split()
a = int(a)
b = int(b)
print(a<b) #a가 b보다 작으면 Ture, 그렇지 않은 경우 False
print(a==b) #a와 b가 같으면 Ture, 그렇지 않은 경우 False'
print(a<=b) #b가 a보다 크거나 같으면 Ture, 그렇지 않은 경우 False
print(a!=b) #a와 b가 다르면 Ture, 그렇지 않은 경우 False
# 비교/관계연산자 종류 : <, >, <=, >=, ==(같다), !=(다르다) 

#--------------------------------------------------------
#logical operation (논리연산)

#참 거짓 평가
n = int(input())
print(bool(n)) #bool(A) = A가 참이면 Ture, 거짓이면 False를 출력

#참 거짓 바꾸기
a = bool(int(input())) #겹쳐 작성하면 계산/처리/평가된다 (input() -> int() -> bool())
print(not a) #not a = a의 반댓값 (Ture -> False, False -> Ture)

#둘 다 참일 경우만 참 (AND)
a, b = input().split()
print(bool(int(a)) and bool(int(b))) #a와 b 모두 Ture일 때 Ture 출력

#하나라도 참이면 참 (OR)
a, b = input().split()
print(bool(int(a)) or bool(int(b))) #a와 b중 하나라도 Ture면 Ture 출력

#서로 다르면 참 (XOR)
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d)) #a와 b가 다르면 Ture 출력 

#참/거짓이 서로 같으면 참 (XNOR)
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(((not a) and (not b)) or (a and b)) #a와 b 둘 다 False 혹은 Ture면 Ture 출력

#둘 다 거짓이면 참 (NOR)
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not(a or b)) # 둘 다 False면 Ture 출력
# not(A or B) = not A and not B 

#-------------------------------------------
#bitwise logical operators(비트단위논리연산)

#비트단위 NOT 출력
a = int(input())
print(~a)

#비트단위 AND 출력
a, b = input().split()
print(int(a) & int(b))

#비트단위 OR 출력
a, b = input().split()
print(int(a) | int(b))

#비트단위 XOR 출력
a, b = input().split()
print(int(a) ^ int(b))

#비트단위 연산자 종류 : ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor), <<(bitwise left shift), >>(bitwise right shift)

#2023-07-21

#Ternary Operator (3항연산자)
#"x if C else y" 
# C : Ture or False 를 평가할 조건식
# x : C의 결과가 Ture 일 때 사용할 값
# y : C의 결과가 False 일 때 사용할 값

#큰 값 출력
a, b = input().split()
a = int(a)
b = int(b)
c = (a if(a>=b) else b) # a>=b의 결과가 참 -> a 출력 // 거짓 -> b 출력
print(c)

#가장 작은 값 출력 (3항 연산자 중첩)
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
min = ((a if(a<b) else b) if ((a if(a<b) else b)<c) else c)
print(min)
