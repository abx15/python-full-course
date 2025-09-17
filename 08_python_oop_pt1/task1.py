# create a class employee with attributes name , id , and salary.Add a method todiplay the emplayee details


class Employee:
    def __init__(self, name, emp_id, salary):
        self.empId = emp_id
        self.empName = name
        self.empSalary = salary

    def display(self):
        print(f"Empolyee Name: {self.empName}")
        print(f"Empolyee ID: {self.empId}")
        print(f"Empolyee Salary: {self.empSalary}")


employee1 = Employee("Ram", "101", 20000)
employee2 = Employee("Soni", "102", 20000)

employee1.display()
employee2.display()
