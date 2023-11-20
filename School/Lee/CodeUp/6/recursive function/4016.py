def gcd(m, n):
  r = int(m % n)
  if r == 0:
    return n
  else:
    return gcd(n, r)


if __name__ == "__main__":
  a, b, c = map(int, input().split())
  k = gcd(a, b)
  print(gcd(k, c))

