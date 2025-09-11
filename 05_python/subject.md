# 📘 Python Tuples, Dictionaries & Sets

## 1️⃣ Tuples in Python

👉 A **tuple** is an ordered, immutable collection of items.

- Ordered → Elements have a defined sequence.
- Immutable → You cannot change or update tuple elements after creation.
- Tuples can store duplicate items.

### ✅ Creating Tuples

```python
# Different ways to create a tuple
tuple1 = (10, 20, 30)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (10, "hello", 3.14, True)

print(tuple1)   # (10, 20, 30)
print(tuple2)   # ('apple', 'banana', 'cherry')
print(tuple3)   # (10, 'hello', 3.14, True)
```

### ✅ Tuple Operations

```python
t = (1, 2, 3, 4, 5)

print(t[0])        # Access → 1
print(t[-1])       # Access last → 5
print(len(t))      # Length → 5
print(t.count(2))  # Count → 1
print(t.index(4))  # Index → 3

```

#### ⚠️ Tuples are immutable:

```python
t = (1, 2, 3)
# t[0] = 99   ❌ Error

```

## 2️⃣ Dictionaries in Python

- 👉 A dictionary is an unordered collection of key-value pairs.

- Keys must be unique and immutable.

- Values can be of any type (even lists/other dictionaries).

- Dictionaries are mutable → you can add, update, or delete items.

### ✅ Creating Dictionaries

```python
student = {
    "name": "Arun",
    "age": 21,
    "course": "Python"
}

print(student)
# {'name': 'Arun', 'age': 21, 'course': 'Python'}
```

### ✅ Accessing Values
```python
print(student["name"]) # Arun
print(student.get("age")) # 21
```
### ✅ Updating & Adding

```python
student["age"] = 22          # Update
student["city"] = "Delhi"    # Add new key
print(student)
#{'name': 'Arun', 'age': 22, 'course': 'Python', 'city': 'Delhi'}
```

### ✅ Deleting

```python
del student["course"]       # Delete by key
print(student)

student.pop("city")         # Remove key and return value
print(student)
```

### ✅ Dictionary Methods

```python
print(student.keys())    # dict_keys(['name', 'age'])
print(student.values())  # dict_values(['Arun', 22])
print(student.items())   # dict_items([('name', 'Arun'), ('age', 22)])
```

## 3️⃣ Sets in Python

- 👉 A set is an unordered collection of unique elements.

- No duplicate values allowed.

- Unordered → No indexing or slicing.

- Useful for mathematical set operations (union, intersection, difference).

### ✅ Creating Sets

```python
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)   # {'apple', 'banana', 'cherry'}  (duplicate removed)

empty_set = set()   # Correct way to make an empty set
```

### ✅ Adding & Removing

```python
fruits.add("orange")
fruits.remove("banana")
print(fruits)
```

### ✅ Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))         # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # {3, 4}
print(a.difference(b))    # {1, 2}
```

## 📝 Quick Comparison

- **Feature: Ordered**
  - Tuple → ✅ Yes
  - Dictionary → ❌ No (Python 3.7+ preserves insertion order)
  - Set → ❌ No

- **Feature: Mutable**
  - Tuple → ❌ No
  - Dictionary → ✅ Yes
  - Set → ✅ Yes

- **Feature: Duplicates**
  - Tuple → ✅ Allowed
  - Dictionary → ✅ Keys unique, values can duplicate
  - Set → ❌ Not allowed

- **Feature: Access**
  - Tuple → By index
  - Dictionary → By key
  - Set → Not possible (unordered)

