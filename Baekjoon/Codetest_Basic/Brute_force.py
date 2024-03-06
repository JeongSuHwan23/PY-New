#일곱 난쟁이
h = []
for i in range(9):
  h.append(int(input()))

h.sort()

h_sum = sum(h)

for i in range(len(h)):
  for j in range(i+1, len(h)):
    if h_sum - h[i] - h[j] == 100:
      for k in range(len(h)):
        if k == j or k == i:
          pass
        else:
          print(h[k])
      exit()

#n과 m (1)
n,m = list(map(int,input().split()))
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()

#n과 m (2)
def dfs(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
  
  for i in range(start, n+1):
    if i not in s:
      s.append(i)
      dfs(i+1)
      s.pop()
      
n, m = list(map(int,input().split()))
s = []
dfs(1)

#n과 m (3)
def dfs():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  
  for i in range(1, n+1):
    s.append(i)
    dfs()
    s.pop()
      
n, m = map(int,input().split())
s = []
dfs()

#n과 m (4)
def dfs(t):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  
  for i in range(1, n+1):
    if i >= t:  
      s.append(i)
      dfs(i)
      s.pop()
      
n, m = map(int,input().split())
s = []
dfs(0)

#n과 m (5)
def dfs():
  if len(box) == m:
    print(' '.join(map(str, box)))
    return
  
  for i in range(n):  
    if numbers[i] in box:
      continue
    box.append(numbers[i])
    dfs()
    box.pop()
        
n, m = map(int,input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()
box = []
dfs()