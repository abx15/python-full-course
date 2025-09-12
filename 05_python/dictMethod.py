d = {
    "name": "Arun",
    "age": 21,
    "courseName": ["Python", "JavaScript", "PHP", "MERN"],
}

print(d.get("email", "nothing@gmail.com"))



# Dictionary Example with All Inbuilt Methods

students = {
    "st1": {"name": "Arun", "age": 21},
    "st2": {"name": "Rohit", "age": 22},
    "st3": {"name": "Priya", "age": 20},
}

print("Original Dictionary:", students)

# 1. keys(), values(), items()
print("\nKeys:", students.keys())
print("Values:", students.values())
print("Items:", students.items())

# 2. get()
print("\nGet st1:", students.get("st1"))
print("Get st5 (not exist):", students.get("st5", "Not Found"))

# 3. copy()
copy_dict = students.copy()
print("\nCopy of Dictionary:", copy_dict)

# 4. fromkeys()
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("\nFromkeys Example:", new_dict)

# 5. pop()
removed = students.pop("st3")
print("\nAfter pop('st3'):", students)
print("Removed Item:", removed)

# 6. popitem()
last_item = students.popitem()
print("\nAfter popitem():", students)
print("Removed Last Item:", last_item)

# 7. setdefault()
students.setdefault("st4", {"name": "Neha", "age": 23})
print("\nAfter setdefault(st4):", students)

# 8. update()
students.update({"st5": {"name": "Aman", "age": 24}})
print("\nAfter update(st5):", students)

# 9. clear()
students.clear()
print("\nAfter clear():", students)
