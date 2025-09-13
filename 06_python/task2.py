# write a function that takes a list and returns only the even numbers

def evenNumbers(lst):

    finalList = [i for i in lst if i % 2 == 0]     # list comprehension
    return finalList

    # finalList = []   
    # for i in lst:
    #     if i % 2 == 0:
    #         finalList.append(i)
    # return finalList

output = evenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Even numbers are:", output)


