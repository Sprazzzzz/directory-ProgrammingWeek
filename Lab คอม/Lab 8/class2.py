students = []

class Score:

    def __init__(self, math, physics, chemistry, biology, science, english):
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.science = science
        self.english = english

    def show(self):
        print(f"Math: {self.math}")
        print(f"Physics: {self.physics}")
        print(f"Chemistry: {self.chemistry}")
        print(f"Biology: {self.biology}")
        print(f"Science: {self.science}")
        print(f"English: {self.english}")

    def average(self):
        return (self.math + self.physics + self.chemistry + self.biology + self.science + self.english) / 6

student1 = Score(90, 85, 92, 88, 91, 87)
student2 = Score(78, 82, 80, 75, 79, 81)
student3 = Score(95, 90, 93, 89, 94, 92)
student4 = Score(85, 88, 84, 86, 87, 89)
student5 = Score(70, 75, 72, 68, 71, 74)

students.append(student1)
students.append(student2)   
students.append(student3)
students.append(student4)
students.append(student5)

average_scores = []
for student in students:
    average = student.average()
    average_scores.append(average) 

highest_average = max(average_scores)
highest_average_index = average_scores.index(highest_average)

lowest_average = min(average_scores)
lowest_average_index = average_scores.index(lowest_average)

print("Student with the highest average score:")
print("Average Score:", highest_average)
students[highest_average_index].show()

print("\nStudent with the lowest average score:")
print("Average Score:", lowest_average)
students[lowest_average_index].show()
