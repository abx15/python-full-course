# Original sets
my_set = {1, 2, 3, 4, 5}
print("Original my_set:", my_set)

my_new_set = set([1, 2, 3, 5, 9, 23, 12, 4, 5])
print("Original my_new_set:", my_new_set)

# 1. add()
my_set.add(10)
print("\nAfter add(10):", my_set)

# 2. update() → multiple elements add
my_set.update([20, 30])
print("After update([20, 30]):", my_set)

# 3. remove() → element remove (error if not exist)
my_set.remove(30)
print("After remove(30):", my_set)

# 4. discard() → element remove (no error if missing)
my_set.discard(50)
print("After discard(50):", my_set)

# 5. pop() → removes random element
popped = my_set.pop()
print("After pop():", my_set, " | Popped:", popped)

# 6. clear() → remove all elements
temp = my_set.copy()
temp.clear()
print("After clear():", temp)

# 7. copy() → shallow copy
copy_set = my_new_set.copy()
print("Copy of my_new_set:", copy_set)

# 8. union() → combine sets
print("\nUnion:", my_set.union(my_new_set))

# 9. intersection() → common elements
print("Intersection:", my_set.intersection(my_new_set))

# 10. difference() → elements in my_set but not in my_new_set
print("Difference (my_set - my_new_set):", my_set.difference(my_new_set))

# 11. symmetric_difference() → elements in either set but not both
print("Symmetric Difference:", my_set.symmetric_difference(my_new_set))

# 12. issubset()
print("\nissubset:", {1, 2}.issubset(my_new_set))  # True if all elements inside

# 13. issuperset()
print("issuperset:", my_new_set.issuperset({1, 2}))  # True

# 14. isdisjoint()
print("isdisjoint:", my_set.isdisjoint({100, 200}))  # True (no common elements)
