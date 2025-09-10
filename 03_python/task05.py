# count the degits in a number

num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10  # last digit hatao
        count += 1  # count badhao

print("Number of digits:", count)
