#재귀 (1~n)
def p(n):
    if n < 1:
        return
    p(n - 1)
    print(n)

def main():
    m = int(input())
    p(m)

if __name__ == "__main__":
    main()

#재귀 (1~n 역순)
def f(k):
    if k == 0:
        return
    print(k)
    f(k - 1)

def main():
    n = int(input())
    f(n)

if __name__ == "__main__":
    main()

#두 수 사이 홀수
def f(n, m):
    if n>m:
        return
    if n%2!=0:
        print(n)
    f(n+1, m)

def main():
    a, b = map(int,input().split())
    f(a, b)

if __name__=="__main__":
    main()

#팩토리얼
def f(a):
    if(a==1):
        return 1
    return a * f(a-1)

def main():
    n = int(input())
    print(f(n))

if __name__=="__main__":
    main()

#2진수 변환
def f(a):
    if a>1:
        f(a//2)
    print(a%2, end="")

def main():
    n = int(input())
    f(n)

if __name__=="__main__":
    main()

#하노이 탑
def hanoi(n, source, auxiliary, target):
    if n > 0:
        hanoi(n-1, source, target, auxiliary)

        print(f"Disk {n} : {source} to {target}")

        hanoi(n-1, auxiliary, source, target)

def main() :
    n = int(input())
    hanoi(n, 'A', 'B', 'C')

if __name__=="__main__":
    main()

#숫자 로테이션
n = int(input())
num_input = input().split()  # 공백을 기준으로 입력을 분할하여 리스트로 저장

num = [0] * 10000
a = 0

for i in range(1, n + 1):
    num[i] = int(num_input[i - 1])  # 분할된 값을 정수로 변환하여 리스트에 저장
    num[i + n] = num[i]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(num[j + a], end=" ")
    print()
    a += 1
