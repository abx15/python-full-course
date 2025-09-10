year = eval(input("Enter The Year: "))

if year % 4 == 0 and year % 100 != 0:
    print("Its A leap Year")
elif year % 400 == 0:
    print("Its a leap year")
else:
    print("Normal Year")
