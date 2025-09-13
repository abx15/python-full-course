# sum all values prices = {'apple': 100, 'banana':40, 'cherry': 60}

prices = {"apple": 100, "banana": 40, "cherry": 60}

allValues = prices.values()
print(sum(allValues))


# or 


total = 0
for value in prices.values():
    total += value

print(total)