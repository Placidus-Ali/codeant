# Add new students to the List

student = ["Ada", "John"]
print(student)

# using append()
student.append("Musa")
print(student)

# using insert()
student.insert(1, "James")
print(student)




# to add more than one items we use extend()
student = ["Ada", "John"]
new_student = ["Mary", "James"]

student.extend(new_student)
print(student)