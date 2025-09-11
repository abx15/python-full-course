# pan card validation

import re

userInput = input("Enter your PAN card number: ")

panNumber = userInput.upper()

if (
    len(panNumber) == 10
    and panNumber[0:5].isalpha()
    and panNumber[5:9].isdigit()
    and panNumber[9].isalpha()
):
    print("Valid PAN card number")
else:
    print("Invalid PAN card number")
