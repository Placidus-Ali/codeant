class Student: # This is the Class called Student
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("-------------------")

# Creating the Objects
student1 = Student("Alice", 12, "Jss1")
student2 = Student("Bob", 13, "JSS2")
student3 = Student("Jane", 14, "Jss3")
student4 = Student("Praise", 15, "SSS1")
student5 = Student("Miracle", 16, "SSS2")
student6 = Student("Amaka", 17, "SSS3")

# priniting the attributes of the Object
student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()
student5.display_info()
student6.display_info()
