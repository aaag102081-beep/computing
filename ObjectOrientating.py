# #class Animal:
#     number_legs=None
#     colour=None

# #Pig=Animal()
# #Pig.weight="70kg"

# #print(Pig.weight)

# #class=blueprint/plan of creating objects
# #object=instance of class

class Human:
    name = None
    height = None
    color = None

    def __init__(self,givenName,givenColor,givenHeight): #contructor function (__init__)
        self.name = givenName
        self.color = givenColor
        self.height = givenHeight
    
    def __str__(self):
        return f"Humans are a type of animal"

    def swim(self):
        return f"I can swim {self.height} lengths of a pool"

    def introduce(self):
        return f"Hi my name is {self.name} and I am {self.height}ft long"


human1 = Human('Raj',"Red",4)
human2 = Human("Saumya","yellow",5)
human3 = Human("Alice", "green", 10)

# print(human2.introduce())
# print(human3.swim())
print(human3)