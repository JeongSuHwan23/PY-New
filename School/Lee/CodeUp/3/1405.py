if __name__ == "__main__" :
    n = int(input())
    num_input = input().split()  # 공백을 기준으로 입력을 분할하여 리스트로 저장
    num = [0] * 10000
    a = 0

    for i in range(1, n + 1):
        num[i] = int(num_input[i - 1])  # 분할된 값을 정수로 변환하여 리스트에 저장
        num[i + n] = num[i]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(num[j + a], end=" ")
        print()
        a += 1