class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: Php{self.salary}")

employee1 = Employee("Nathasia Jessa", "Cybersecurity Specialist", 140000)

employee1.give_raise(90000)
employee1.display_employee()
