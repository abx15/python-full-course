# basic function


def showCompanyName():
    print("Welcome to ABC Corporation")


showCompanyName()


# function with parameter


def showEmployeeName(name):  # name is parameter
    print("Employee Name:", name)


showEmployeeName("John Doe")  # 'John Doe' is argument


# Return value from function


def addNumbers(a, b):
    return a + b


result = addNumbers(5, 10)
print("Sum is:", result)


# Default parameter values


def greetUser(name="Guest"):
    print("Hello,", name)


greetUser()  # Uses default value
greetUser("Alice")  # Overrides default value

# multiple value with one parameter


def displayScores(*scores):
    print("Scores:", scores)


displayScores(85, 90, 78, 92)


# with loop
def displayItems(*items):
    for item in items:
        print("Item:", item)


displayItems("Apple", "Banana", "Cherry")

# Local Variable


def displayLocalVar():
    locals_var = "I am local"
    print(locals_var)


displayLocalVar()

# Global Variable

gl = "i am global"


def displayGlobalVar():
    print(gl)

displayGlobalVar()


def displayGlobalVar2():
    gl = "i am local now"
    print(gl)

displayGlobalVar2()


# lambda function
square = lambda x: x * x
print("Square of 5 is:", square(5))

# Recursive function

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print("Factorial of 5 is:", factorial(5))