age = eval(input("Enter your Age: "))

if age < 0:
    print("Invalid Age ")
elif age < 18:
    print("You cannot vote now ")
    print("Your age:", age)
elif age == 18:
    print("You just became eligible! ")
    print("Your age:", age)
elif age > 18 and age < 100:
    print("You can vote ")
    print("Your age:", age)
else:
    print("Age not valid, please check again ")

