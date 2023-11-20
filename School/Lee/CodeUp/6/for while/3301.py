if __name__ == "__main__":
  money = int(input())
  count = int(0)

  for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
    if money // i != 0:
      count = count + (money // i)
      money = money % i

  print(count)