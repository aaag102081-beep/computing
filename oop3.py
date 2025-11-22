class Student:
    name = None
    weight = None
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        print("Student created")
    # method overloading
    def introduction(self):
        print(f"I am a student and my name is {self.name}")
        print("I am a student and my name is " + self.name)
 

class Boy(Student):
    gender = "M"
    def __init__(self,name,weight,gender):
        super().__init__(name,weight)
        self.gender = gender
        print("Boy is created")

    def introduction(self,name):
        print("I am a boy ")

student1 = Student("Gaurav",24)
student1.introduction()



# student1.introduction("Rohan")