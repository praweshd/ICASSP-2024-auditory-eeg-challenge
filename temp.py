class Animal:

    def __init__(self, bark, meow):
        self.bark = bark
        self.meow = meow

class Dog(Animal):

    def __init__(self):
        super().__init__(True, False)

class Cat(Animal):
    
    def __init__(self):
        super().__init__(False, True)

# class DogCat(Dog, Cat):
#     def __init__(self):
#         super(DogCat, self).__init__()

cat = Cat()
# dog = Dog()
# abomination = DogCat()
# print(cat.call)
# print(dog.call)
print(cat.bark, cat.meow)

# musi = Musi("Musi!!", "HaHeng")
# print(musi.name, musi.call)

# class First(object):
#     def __init__(self):
#         print("first")

# class Second(First):
#     def __init__(self):
#         print("second")

# class Third(First):
#     def __init__(self):
#         print("third")

# class Fourth(Second, Third, First):
#     def __init__(self):
#         # super(Fourth, self).__init__()
#         super(Third, self).__init__()
#         # print("that's it")

# fourth = Fourth()