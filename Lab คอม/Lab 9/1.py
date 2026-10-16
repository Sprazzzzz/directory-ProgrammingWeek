class Person:
    def __init__(self, name, address, weight, height, age):
        self.name = name
        self.address = address
        self.weight = weight
        self.height = height    
        self.age = age

    def getBMI(self):
        return self.weight / (self.height ** 2)

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"Age: {self.age} years")
        print(f"BMI: {self.getBMI():.2f}")

class Employee(Person):
    def __init__(self, name, address, weight, height, age, employee_id, department, salary):
        super().__init__(name, address, weight, height, age)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def showInfo(self):
        super().showInfo()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:.2f}") 

employee1 = Employee("John Doe", "123 Main St", 70, 1.75, 30, "E001", "Engineering", 75000)
employee1.showInfo()
