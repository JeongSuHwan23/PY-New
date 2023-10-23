def hanoi(n, source, auxiliary, target):
    if n > 0:
        hanoi(n-1, source, target, auxiliary)
        print(f"Disk {n} : {source} to {target}")
        hanoi(n-1, auxiliary, source, target)

if __name__=="__main__":
    n = int(input())
    hanoi(n, 'A', 'B', 'C')