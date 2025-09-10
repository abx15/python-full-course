# Simple Calculator using if elif else

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


choice = input("Enter your choice (+ ,- , *, / ): ")


if choice == "+":
    print("Result:", num1 + num2)
elif choice == "-":
    print("Result:", num1 - num2)
elif choice == "*":
    print("Result:", num1 * num2)
elif choice == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")
