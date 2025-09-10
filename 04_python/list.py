# -----------------------------
# Python Lists
# -----------------------------

# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.5, True]

print("Fruits List:", fruits)
print("Numbers List:", numbers)
print("Mixed List:", mixed)

# -----------------------------
# Accessing elements
# -----------------------------
print("\nAccessing Elements:")
print("fruits[0]:", fruits[0])      # apple
print("fruits[1]:", fruits[1])      # banana
print("fruits[-1]:", fruits[-1])    # mango (last element)
print("fruits[1:3]:", fruits[1:3])  # ['banana', 'cherry'] → slicing

# -----------------------------
# Modifying elements
# -----------------------------
print("\nModifying Elements:")
fruits[1] = "blueberry"
print("After modifying index 1:", fruits)

# -----------------------------
# Adding elements
# -----------------------------
print("\nAdding Elements:")
fruits.append("orange")     # add at end
print("After append:", fruits)

fruits.insert(2, "kiwi")    # insert at index
print("After insert:", fruits)

# -----------------------------
# Removing elements
# -----------------------------
print("\nRemoving Elements:")
fruits.remove("apple")      # remove by value
print("After remove 'apple':", fruits)

popped = fruits.pop()       # remove last element
print("After pop():", fruits, " | Popped element:", popped)

del fruits[1]               # delete by index
print("After del index 1:", fruits)

fruits.clear()              # empty the list
print("After clear():", fruits)

# -----------------------------
# Re-creating fruits list
# -----------------------------
fruits = ["apple", "banana", "cherry", "mango"]

# -----------------------------
# Looping through a list
# -----------------------------
print("\nLooping Example:")
for f in fruits:
    print(f)

# With index
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# -----------------------------
# List Comprehension
# -----------------------------
print("\nList Comprehension:")
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# -----------------------------
# Sorting
# -----------------------------
print("\nSorting Example:")
numbers = [40, 10, 50, 20, 30]
print("Original Numbers:", numbers)

numbers.sort()
print("Ascending Sort:", numbers)

numbers.sort(reverse=True)
print("Descending Sort:", numbers)

fruits = ["banana", "apple", "mango", "cherry"]
fruits.sort()
print("Sorted Fruits:", fruits)

# -----------------------------
# Built-in Functions
# -----------------------------
print("\nBuilt-in Functions:")
numbers = [10, 20, 5, 40, 15]

print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Index of 40:", numbers.index(40))
print("Count of 10:", numbers.count(10))

# -----------------------------
# Copying a list
# -----------------------------
print("\nCopy Example:")
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print("List1:", list1)
print("List2:", list2)

# -----------------------------
# Nested Lists
# -----------------------------
print("\nNested List:")
nested = [[1, 2], [3, 4], [5, 6]]
print("Nested List:", nested)
print("Access nested element [1][0]:", nested[1][0])  # 3
