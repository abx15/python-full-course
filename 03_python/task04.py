# reverse a number using while loop 

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10          # last digit nikalo
    reverse = reverse * 10 + digit  # digit ko reverse number me jodo
    num //= 10                # last digit hatao

print("Reversed number:", reverse)