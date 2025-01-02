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
Employee.__dict__["increase_salary"](employee1,20)
print(employee1.salary)