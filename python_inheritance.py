class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    def display_employee_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")

class EmployeeSalary(Employee):
    def __init__(self, name, age, department, salary):
        super().__init__(name, age, department)
        self.salary = salary
    def display_employee_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}")
class EmployeeDepartment(Employee,):
    def __init__(self, name, age, department):
        super().__init__(name, age, department)

employee = EmployeeDepartment("Swetha", 25, "IT")
print(EmployeeDepartment("Swetha", 25, "IT").display_employee_details())
employe_salary = EmployeeSalary("Swetha", 25, "IT", 8000)
print(employe_salary.name)
employe_salary.display_employee_details()


# Abstract 
 
from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def display_details(self):
        pass
    @abstractmethod
    def display_name(self):
        pass
    @abstractmethod
    def display_age(self):
        pass
    @abstractmethod
    def display_salary(self):
        pass

class PersonDetails(Person):
    def display_details(self, name, age):
        print(f"Name: {name}, Age: {age},")
    def display_name(self,name):
        print(f"Name: {name}")
    def display_age(self,age):
        print(f"Age: {age}")
    def display_salary(self, salary):
        print(f"Salary: {salary}")
person = PersonDetails()
person.display_details("Swetha", 25)



class ParkingTicket:
    def get_vechical_number(self, number):
        return number
    def get_vechical_type(self, vechicle_type):
        return vechicle_type
class PrakingTime:
    def get_time_in_minutes(self, time):
        return time
    def get_time_in_hours(self, time):
        return

class ParkingTicketGenerator(ParkingTicket, PrakingTime):
    def generate_parking_ticket(self, number, vechicle_type, time):
        print(f"Vechicle Number: {self.get_vechical_number(number)}")
        print(f"Vechicle Type: {self.get_vechical_type(vechicle_type)}")
        print(f"Time: {self.get_time_in_minutes(time)}")
        print(f"Time: {self.get_time_in_hours(time)}")
parking_ticket = ParkingTicketGenerator()
parking_ticket.generate_parking_ticket("TS 08 1234", "Car", 30)

