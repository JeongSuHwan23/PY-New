class Grade:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def s_grade(self):
        if self.score>=90 :
            self.grand = "A"
        elif self.score>=80 :
            self.grand = "B"
        else :
            self.grand = "C"

    def __str__(self):
        return "%s: %c등급" %(self.name, self.grand)

if __name__ == "__main__" :
    a1 = Grade("나영", 89)
    a1.s_grade()
    print(a1)