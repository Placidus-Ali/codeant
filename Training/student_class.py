class Student: # This is the Class called Student
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Creating the Objects
student1 = Student("Alice", 12, "Jss1")
student2 = Student("Bob", 13, "JSS2")
student3 = Student("Jane", 14, "Jss3")
student4 = Student("Praise", 15, "SSS1")
student5 = Student("Miracle", 16, "SSS2")
student6 = Student("Amaka", 17, "SSS3")

# priniting the attributes of the Object
print(student1.name)
print(student1.age)
print(student1.grade)

print(student6.name)