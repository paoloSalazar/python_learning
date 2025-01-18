def average(a:int, b:int, c:int) -> float:
    return (a + b + c) / 3

print(average(1, 5, 7))


# Two int arguments, return a float
def plus(num1: int, num2: int) -> int:
    return num1 + num2

# Add default value for an argument after the type annotation
def f(num1: int, my_float: float =3.5) -> float:
    return num1 + my_float


age: int = 1
# In Python 3.5 or earlier use a comment
age = 1 # type: int