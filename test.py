h = []
for i in range(9):
  temp = input()
  h.append(int(temp))
h.sort()
h_sum = sum(h)
for i in range(len(h)):
	for j in range(i+1, len(h)):
    if h_sum - i - j == 100:
      for j in range(9):
  