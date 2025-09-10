num = eval(input("Enter Your number: "))

if num % 3 == 0 and num % 5 != 0:
    print("devide by 3 but not devide by 5")

elif num % 3 != 0 and num % 5 == 0:
    print("Devide by 5 but not devide by 3")
elif num % 3 == 0 and num % 5 == 0:
    print("divide by both")
else:
    print("not devide by both")
