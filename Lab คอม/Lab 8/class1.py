class Student:

    def __init__(self, student_id, name, course, age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = age

    def show(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Age: {self.age}")

students = []

student1 = Student(6901012610463, "Nuttakorn Arkartvipart", "Cpr.e", 18)
student2 = Student(6901012610464, "John Doe", "Cpr.e", 19)
student3 = Student(6901012610465, "Jane Smith", "Cpr.e", 17)
student4 = Student(6901012610466, "Alice Johnson", "Cpr.e", 20)
student5 = Student(6901012610467, "Bob Brown", "Cpr.e", 21)

students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)
students.append(student5)

youngest_student = students[0]

for student in students:
    if student.age < youngest_student.age:
        youngest_student = student

print("Youngest Student:")
youngest_student.show()

