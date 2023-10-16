#순위 구하기
n = int(input())

d = input().split()

for i in range(n) :
    d[i] = int(d[i])
    d.append(d[i])

rank = []
for i in range(n) :
    temp = 1
    for j in range(i, n+i) :
            if d[i] < d[j] :
                temp+=1
    rank.append(temp)    

for i in range (n) :
    print(d[i], rank[i], end=" ")
    print()

#타자기
import random
import time 

WORD_LIST=[
    'Hello World',
    'Okay Okay',
    'GangGangGang'
]
random.shuffle(WORD_LIST)

for i in WORD_LIST:
    start_time = time.time()
    user_input  = str(input(i+'\n')).strip()
    end_time = time.time()-start_time

    correct = 0
    for index, c in enumerate(user_input) :
        if index >= len(i) :
            break
        if c == i[index]:
            correct+=1
    
    total_len=len(i)
    c=correct/total_len*100
    e=(total_len-correct)/total_len*100
    speed=correct/end_time*60

    print("speed : {:0.2f} correct : {:0.2f} not correct : {:0.2f}".format(speed, c, e))
    
#기본 class
class BSSM :
    def __init__(self, task, age, name) :
        self.team="부소마"
        self.task=task
        self.age=age
        self.name=name
    
    def intro(self) :
        print("안녕하세요, %s에서 %s를 담당하고 있는 %s살 %s입니다. " %(self.team, self.task, self.age, self.name))

if __name__ == "__main__" :
    a = BSSM("A", "17", "정수환")
    a.intro()
    