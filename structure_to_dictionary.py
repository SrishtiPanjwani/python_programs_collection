# Structure-to-Dictionary Conversion
# A Python class is used as a structure-like container for student data.

class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

student = Student("Aarav", 101, "Computer Science")

# vars() returns the object's attributes as a dictionary.
student_dict = vars(student)

print("Dictionary:", student_dict)
