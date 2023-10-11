# 짝수 합
def sum(k):
    print(k)
    if k <= 0:
        return 0
    return k + sum(k - 2)

def main():
    n = int(input())
    if n % 2 == 1:
        n -= 1
    print(sum(n))

if __name__ == '__main__':
    main()

#이상한 출석
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

d = []
for i in range(24) :
  d.append(0)

for i in range(n) :
  d[a[i]] += 1

for i in range(1, 24) :
  print(d[i], end=' ')

#바둑돌
d=[]                        #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20) :
  d.append([])         #리스트 안에 다른 리스트 추가해 넣기
  for j in range(20) : 
    d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()                          #줄 바꿈


def pop(sum):
    global myList
    if myList:
        pop(sum+myList.pop())
    else:
        print(sum)
        return 0

if __name__ == "__main__":
    myList = input().split()
    myList = [int(x) for x in myList]
    pop(0)

