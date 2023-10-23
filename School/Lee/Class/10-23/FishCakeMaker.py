class FishCakeMaker :
    def __init__(self, **kwargs):
        self.size=10
        self.flavor="팥"
        self.price=100

        if "size" in kwargs :
            self.size = kwargs.get("size")
        if "flavor" in kwargs :
            self.flavor = kwargs.get("flavor")
        if "price" in kwargs:
                self.price = kwargs.get("price")

    def show(self):
        print("붕어빵 크기 : {}".format(self.size))
        print("붕어빵 종류 : {}".format(self.flavor))
        print("붕어빵 가격 : {}".format(self.price))
        print()

if __name__ == "__main__" :
    fish1 = FishCakeMaker()
    fish2 = FishCakeMaker(size=20, price=200)
    fish3 = FishCakeMaker(size=20, flavor="슈크림")

    fish1.show()
    fish2.show()
    fish3.show()