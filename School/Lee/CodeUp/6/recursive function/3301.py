def k(n, d, i, c):
  if n < 10:
    print(c)
    return
  c += n//d[i]
  k(n%d[i], d, i+1, c)

if __name__ == "__main__":
  n = int(input())
  d = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
  i = int(0)
  count = int(0)
  k(n, d, i, count)
