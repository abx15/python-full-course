# Demonstration of loop control statements: break, continue, and pass

# Break statement example

for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("Loop End")

# Continue statement example

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


print("Loop End")

# Pass statement example

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

print("Loop End")


