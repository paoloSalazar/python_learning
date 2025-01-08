from dataclasses import dataclass


"""Use mypy tool to check attribute type
   pip install mypy"""
@dataclass
class Project:
    """data clases are used to avoid writting all class init method"""
    name: str
    payment: int
    client: str
    
    

# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("Django APP", "20000", "Globomatics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)