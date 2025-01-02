class Developer:
    # tuple used to represent class attr
    __slots__ = ("name", "age", "salary", "framework")

    def __init__(self, name, age, salary, framework):
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework


employee1 = Developer("Ji-soo", 38, 400, "flask")

print(employee1.__slots__)