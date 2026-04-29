#Create a class called Student and create object properties name and grade
class Student:
    def __init__(self, name, grade,genderpronoun,age,address):
        self.name = name
        self.grade = grade
        self.genderpronoun = genderpronoun
        self.age = age
        self.address = address
    def info(self):
        print(f"This is {self.name} and {self.genderpronoun} scored {self.grade} in her test. {self.genderpronoun.capitalize()} is {self.age} years old and lives in {self.address}")    
#Create an object student1 and assign "Lisa" as name and grade "A"
student1 = Student("Lisa", "A","she",7,"Kampala")

#call the info method
student1.info()


