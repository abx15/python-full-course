
print("---- Simple Calculator ----")
print("Operations: +  -  *  /  %  **  //")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator: ")

match op:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero ")
    case "%":
        print(f"{num1} % {num2} = {num1 % num2}")
    case "**":
        print(f"{num1} ** {num2} = {num1 ** num2}")
    case "//":
        if num2 != 0:
            print(f"{num1} // {num2} = {num1 // num2}")
        else:
            print("Error: Division by zero ")
    case _:
        print("Invalid Operator ")
