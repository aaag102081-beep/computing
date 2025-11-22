class Animal:
    legs = None
    wings = None
    
    def __init__(self):
        print("hello world")

    def sleep(self):
        print("I sleep in night")


class Human(Animal):
    legs = 2
    name = None
    def __init__(self,givenName):
        self.name=givenName
        # print("Anaya")
    def sleep(self):
        print("Human dont sleep")

class Student(Human):
        height = None
        rank = None
        def __init__(self,givenHeight):
            self.height= givenHeight
            print("6 ft")
        def rank(self,givenRank):
           self.rank=givenRank

student1=Student(givenHeight)
student1.rank("rank 1")
# human1 = Human('anaya')
# print(human1.name)

