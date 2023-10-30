import random

# 16명의 사람을 표현하는 리스트를 만듭니다.
people = list(range(1, 17))

# 리스트를 무작위로 섞습니다.
random.shuffle(people)

# 4x4 행렬로 자리를 나타냅니다.
matrix = [people[i:i+4] for i in range(0, 16, 4)]

# 자리 바꾸기 후의 결과를 출력합니다.
for row in matrix:
    print(row)
