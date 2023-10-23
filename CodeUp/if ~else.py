#2023-07-21

#if 조건식 :  조건식을 평가해서...
#   실행1      True 인 경우 실행시킬 명령들...
#   실행2
#else :        
#   실행3      False 인 경우 실행시킬 명령들...
#   실행4
#실행5       조건식과 상관없는 다음 명령


#짝수만 출력
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0 : #논리적으로 한 단위로 처리해야하는 경우 콜론(:)을 찍고, 들여쓰기로 작성 // 들여쓰기를 안 하면 print가 실행 안됨
    print(a)
if b%2==0 :
    print(b)
if c%2==0 :
    print(c)

#짝/홀 출력
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0 :
    print("even")
else :
    print("odd")
if b%2==0 :
    print("even")
else :
    print("odd")
if c%2==0 :
    print("even")
else :
    print("odd")

#-/+ 와 짝/홀 구분
n = int(input())
if (n<0) :
    if(n%2==0) :    #if(n<0) : if(n%2==0) == if(n<0 and n%2==0) 
        print('A')
    else :
        print('B')
else :
    if(n%2==0) :
        print('C')
    else :
        print('D')    
