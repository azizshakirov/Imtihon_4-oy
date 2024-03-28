class Employee:
    def __init__(self, name, position, salary) -> None:
        self.name = name
        self.position = position
        self.salary = salary

class Enterprice_employee(Employee):
    def __init__(self, name, position, salary, rating) -> None:
        super().__init__(name, position, salary)
        self.rating = rating
    

    def increase_salary(self):
        if 60 <= self.rating < 75:
            self.salary *= 1.2
        elif 75 <= self.rating < 90:
            self.salary *= 1.4
        elif 90 <= self.rating <= 100:
            self.salary *= 1.6

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Rating: {self.rating}"


employee = []

for i in range(5):
    name = input(f"{i+1}-Name: ")
    position = input(f"{i+1}-Position: ")
    salary = int(input(f'{i+1}-Salary: ')) 
    rating = int(input(f'{i+1}-Rating: ')) 
    employee.append(Enterprice_employee(name, position, salary, rating))
    
for emp in employee:
    emp.increase_salary()
    print(emp)

