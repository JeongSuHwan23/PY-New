def dice(a, b):
  print(a, b)
  if b == 1 or a > 5:
    return

  dice(a + 1, b - 1)


if __name__ == "__main__":
  n = int(input())
  m = 1
  if n > 6:
    m = n - 6
    n = 7
  dice(m, n - 1)