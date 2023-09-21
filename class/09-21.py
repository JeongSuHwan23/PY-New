def jump(n) :
    if (n<1) :
        return 0
    elif (n==1) :
        return 1
    else :
        return jump(n-1) + jump(n-2) + jump(n-3)


def main():
    n = int(input())
    answer = jump(n+1)
    print(answer)

if __name__ == "__main__":
    main()