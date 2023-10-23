class BSSM:
    def __init__(self, task, age, name):
        self.team = "부소마"
        self.task = task
        self.age = age
        self.name = name

    def intro(self):
        print("안녕하세요, %s에서 %s를 담당하고 있는 %s살 %s입니다. " % (self.team, self.task, self.age, self.name))


if __name__ == "__main__":
    a = BSSM("A", "17", "정수환")
    a.intro()
