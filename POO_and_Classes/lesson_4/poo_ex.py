from datetime import date

class Employee:
    # __slots__ = ("name", "age", "_salary")
    minimum_wage = 1000

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self._salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.salary)})"
            )
    
    @property
    def salary(self):
        """getter function example"""
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        """Setter example the funcion name should match with the above method"""
        if salary < Employee.minimum_wage:
            raise ValueError("Minimun wage is $1000")
        self._salary = salary
        # raise ValueError("Read only")
    
    @classmethod
    def change_minimum_wage(cls, new_wage):
        """Used to define method that belons to class not instances"""
        if new_wage > 3000:
            raise ValueError("Company is bankrupt..")
        cls.minimum_wage = new_wage
    
    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

class Tester(Employee):
    def run_tests(self):
        print(f"testing is started by {self.name}...")
        print("Tests are done")

class Developer(Employee):
    __slots__ = ("framework")

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

employee1 = Employee("lauren",44, 1000)
# this assignment is using the setter method defined in the class
employee1.salary = 1200
# print(Employee.__dict__)
# Employee.__dict__["increase_salary"](employee1,20)
# print(employee1.salary)

# print(Employee.minimum_wage)
# Employee.change_minimum_wage(2000)
# print(Employee.minimum_wage)
e = Employee.new_employee("Mary", date(1991,8,12))
print(e.name)
print(e.age)
print(e.salary)