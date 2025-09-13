# suppose there are two lists one containing numbers from 1 to 6 and other  containing numbers from 6 to 1 . Write a program to obtain a list that contains elements obtained by adding corresponding elements of the two lists

list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]
result = [a + b for a, b in zip(list1, list2)]
print("Resultant list after adding corresponding elements:", result)
