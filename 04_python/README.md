# 📘 Python Strings and Lists

## 🔹 1. Strings in Python
### 👉 What is a String?
A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' / ).

Strings are immutable (cannot be changed after creation).

### ✅ Creating Strings
```python
# Different ways to create a string
str1 = 'Hello'
str2 = "World"
str3 = '''This is a 
multi-line string'''

print(str1)
print(str2)
print(str3)
```

**Output:**
```
Hello
World
This is a 
multi-line string
```

### ✅ String Operations
```python
text = "Python"

# Length
print(len(text))        # 6

# Indexing
print(text[0])          # P
print(text[-1])         # n

# Slicing
print(text[0:4])        # Pyth
print(text[2:])         # thon
```

### ✅ Useful String Methods
```python
s = "  hello Python  "

print(s.upper())        # HELLO PYTHON
print(s.lower())        # hello python
print(s.strip())        # hello Python   (removes spaces from start & end)
print(s.replace("Python", "World"))   # hello World
print(s.split())        # ['hello', 'Python']
print("Python" in s)    # True
```

### ✅ Real Example: User Input & String Formatting
```python
name = "Arun"
course = "Python"

print(f"My name is {name} and I am learning {course}.")
```

**Output:**
```
My name is Arun and I am learning Python.
```

---

## 🔹 2. Lists in Python
### 👉 What is a List?
A list is a collection of items (elements) that can be of different data types.

Lists are mutable (can be changed after creation).

Defined using square brackets [ ].

### ✅ Creating Lists
```python
numbers = [10, 20, 30, 40]
mixed = [1, "Hello", 3.5, True]

print(numbers)
print(mixed)
```

**Output:**
```
[10, 20, 30, 40]
[1, 'Hello', 3.5, True]
```

### ✅ List Operations
```python
nums = [10, 20, 30, 40, 50]

# Length
print(len(nums))     # 5

# Indexing
print(nums[0])       # 10
print(nums[-1])      # 50

# Slicing
print(nums[1:4])     # [20, 30, 40]
```

### ✅ Adding / Removing Elements
```python
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")       # Add at end
fruits.insert(1, "orange")   # Insert at index 1
print(fruits)                # ['apple', 'orange', 'banana', 'cherry', 'mango']

fruits.remove("banana")      # Remove by value
popped = fruits.pop()        # Remove last element
print(fruits)                # ['apple', 'orange', 'cherry']
print("Popped:", popped)     # Popped: mango
```

### ✅ Useful List Methods
```python
nums = [3, 1, 4, 2]

nums.sort()          # [1, 2, 3, 4]
nums.reverse()       # [4, 3, 2, 1]

print(max(nums))     # 4
print(min(nums))     # 1
print(sum(nums))     # 10
```

### ✅ Iterating Over a List
```python
colors = ["red", "green", "blue"]

for c in colors:
    print(c)
```

**Output:**
```
red
green
blue
```

### ✅ Real Example: Shopping Cart
```python
cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Your Cart:", cart)

cart.remove("Mouse")
print("After removing Mouse:", cart)
```

**Output:**
```
Your Cart: ['Laptop', 'Mouse', 'Keyboard']
After removing Mouse: ['Laptop', 'Keyboard']
```

---

## 🎯 Summary

| Feature     | String | List |
|-------------|--------|------|
| Mutability  | Immutable (cannot change directly) | Mutable (can change) |
| Data Type   | Only characters | Can store multiple data types |
| Syntax      | `"Hello"` | `[1, "Hi", 3.5]` |
| Operations  | Indexing, slicing, methods (upper, lower, replace, split) | Indexing, slicing, methods (append, remove, sort, reverse) |
