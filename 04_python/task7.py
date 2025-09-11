list = [10, 40, 20, 48]

# print (max(list))

# or 
maxValue = list[0]

for n in list:
    if n > maxValue:
        maxValue = n

print(maxValue)