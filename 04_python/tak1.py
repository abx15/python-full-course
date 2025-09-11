# Aadhar  number check


userinput = input("Enter your Aadhar number: ")

if userinput.isdigit() and len(userinput) == 16:
    print("Valid Aadhar number")
else:
    print("Invalid Aadhar number")