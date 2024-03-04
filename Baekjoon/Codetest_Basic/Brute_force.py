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

#사탕 게임

