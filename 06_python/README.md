# 📘 Python Functions

Functions in Python are **reusable blocks of code** that can be executed
whenever needed without rewriting them. They make programs **modular,
readable, and maintainable**.

------------------------------------------------------------------------

## 🔹 What is a Function?

A function is a **named block of code** that can take input
(parameters), perform some operations, and return an output (return
value).

------------------------------------------------------------------------

## 🔹 Advantages of Functions

-   Code reusability (no need to rewrite code again and again)\
-   Makes program modular\
-   Easier debugging\
-   Increases readability

------------------------------------------------------------------------

## 🔹 Function Syntax

``` python
def function_name(parameters):
    """docstring (optional)"""
    # code block
    return value
```

### Example:

``` python
def greet(name):
    """This function greets the person passed as parameter"""
    return f"Hello, {name}!"
```

------------------------------------------------------------------------

## 🔹 Types of Functions in Python

1.  **Built-in Functions** → e.g., `print()`, `len()`, `type()`,
    `sum()`\

2.  **User-defined Functions** → functions created by the user\

3.  **Lambda Functions (Anonymous Functions)** → small inline functions

    ``` python
    square = lambda x: x * x
    print(square(5))  # Output: 25
    ```

4.  **Recursive Functions** → a function that calls itself

    ``` python
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n-1)
    print(factorial(5))  # Output: 120
    ```

------------------------------------------------------------------------

## 🔹 Function Parameters

1.  **Positional Arguments**

    ``` python
    def add(a, b):
        return a + b
    print(add(5, 10))  # Output: 15
    ```

2.  **Default Arguments**

    ``` python
    def greet(name="User"):
        return f"Hello, {name}"
    print(greet())       # Output: Hello, User
    print(greet("Arun")) # Output: Hello, Arun
    ```

3.  **Keyword Arguments**

    ``` python
    def student(name, age):
        return f"Name: {name}, Age: {age}"
    print(student(age=20, name="Arun"))
    ```

4.  **Variable-length Arguments**

    -   `*args` → multiple positional arguments\
    -   `**kwargs` → multiple keyword arguments

    ``` python
    def my_func(*args, **kwargs):
        print("Positional:", args)
        print("Keyword:", kwargs)

    my_func(1, 2, 3, name="Arun", age=20)
    # Output: Positional: (1, 2, 3)
    #         Keyword: {'name': 'Arun', 'age': 20}
    ```

------------------------------------------------------------------------

## 🔹 Return Statement

The `return` keyword is used to send output from a function.

``` python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # Output: 20
```

------------------------------------------------------------------------

## 🔹 Best Practices for Functions

✔ Use meaningful names (e.g., `calculate_total`, `get_user_data`)\
✔ Always add a docstring to explain the function\
✔ Keep functions small and focused on one task\
✔ Follow DRY Principle (Don't Repeat Yourself)

------------------------------------------------------------------------

## ✅ Conclusion

Python Functions are powerful tools that make coding easier and more
readable. They help break down large programs into smaller, manageable
parts.
