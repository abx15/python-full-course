# Tuple with numbers
t1 = (10, 20, 30)

# Tuple with strings
t2 = ("apple", "banana", "cherry")

# Mixed data types
t3 = (10, "hello", 3.14, True)

print(t1)
print(t2)
print(t3)


# Single element tuple (comma जरूरी है)
t = (10,)
print(type(t))

# Indexing
t = (100, 200, 300, 400)
print(t[0])
print(t[2])
print(t[-1])

# Tuple methods
t = (1, 2, 3, 2, 4, 2)
print(len(t))
print(t.count(2))
print(t.index(4))

# Real-world example → Coordinates as keys
locations = {
    (25.276987, 55.296249): "Dubai",
    (28.704060, 77.102493): "Delhi",
    (40.712776, -74.005974): "New York"
}

print(locations[(40.712776, -74.005974)])
