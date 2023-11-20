def gcd(m, n):
  r = int(m % n)
  if r == 0:
    print(n)
    return
  else:
    gcd(n, r)


if __name__ == "__main__":
  a, b = map(int, input().split())
  gcd(a, b)
