# -----------------------------
# String Creation
# -----------------------------
str1 = "Hello"
str2 = "hello Arun"
str3 = """ This Is 
multi-line 
string
"""

print("String 1:", str1)
print("String 2:", str2)
print("String 3:", str3)

# -----------------------------
# Accessing characters in a string
# -----------------------------
str4 = "   Hello Arun   "

print("\nOriginal String:", repr(str4))   # repr() spaces clearly show karta hai

# Indexing with positions
print("\nIndexing Example:")
print("str4[0]:", repr(str4[0]))   # First character → " " (space)
print("str4[1]:", repr(str4[1]))   # Second character → " " (space)
print("str4[2]:", repr(str4[2]))   # Third character → " " (space)
print("str4[3]:", str4[3])         # Fourth character → "H"
print("str4[4]:", str4[4])         # "e"
print("str4[5]:", str4[5])         # "l"
print("str4[6]:", str4[6])         # "l"
print("str4[7]:", str4[7])         # "o"
print("str4[8]:", str4[8])         # " " (space)
print("str4[9]:", str4[9])         # "A"
print("str4[10]:", str4[10])       # "r"
print("str4[11]:", str4[11])       # "u"
print("str4[12]:", str4[12])       # "n"
print("str4[13]:", repr(str4[13])) # " " (space)
print("str4[14]:", repr(str4[14])) # " " (space)
print("str4[15]:", repr(str4[15])) # " " (space)

# -----------------------------
# Index chart using loop
# -----------------------------
print("\nIndex chart:")
for i in range(len(str4)):
    print(f"Index {i}: {repr(str4[i])}")

# -----------------------------
# Case Conversion
# -----------------------------
print("\nCase Conversion:")
print("Uppercase:", str4.upper())
print("Lowercase:", str4.lower())

# -----------------------------
# Removing spaces
# -----------------------------
print("\nRemoving Spaces:")
print("strip():", str4.strip())
print("lstrip():", str4.lstrip())
print("rstrip():", str4.rstrip())

# -----------------------------
# Replace
# -----------------------------
print("\nReplace Example:")
print(str4.replace("Arun", "World"))

# -----------------------------
# Split & Join
# -----------------------------
print("\nSplit & Join:")
print(str4.split())          # split into list
print("-".join(str4.split()))  # join with "-"

# -----------------------------
# Checking substrings
# -----------------------------
print("\nCheck Substring:")
print("Arun" in str4)        # True
print("Python" in str4)      # False
print("Hello" not in str4)   # False

# -----------------------------
# Length of string
# -----------------------------
print("\nLength of String:", len(str4))

# -----------------------------
# Find, Index, Startswith, Endswith
# -----------------------------
print("\nFind & Index:")
print("find('Arun'):", str4.find("Arun"))
print("startswith('Hello'):", str4.strip().startswith("Hello"))
print("endswith('Arun'):", str4.strip().endswith("Arun"))

# -----------------------------
# Count occurrences
# -----------------------------
print("\nCount Example:")
print("count('l'):", str4.count("l"))

# -----------------------------
# Capitalize, Title, Swapcase
# -----------------------------
print("\nCapitalize, Title & Swapcase:")
print("capitalize():", str4.capitalize())
print("title():", str4.title())
print("swapcase():", str4.swapcase())

# -----------------------------
# Justify & zfill
# -----------------------------
print("\nFormatting:")
print("center(20, '-'):", str4.strip().center(20, "-"))
print("ljust(20, '-'):", str4.strip().ljust(20, "-"))
print("rjust(20, '-'):", str4.strip().rjust(20, "-"))
print("zfill(5):", "123".zfill(5))

n = "Hello123"
print (n.isalnum()) # True
print (n.isalpha()) # False
print (n.isdigit()) # False
print (n.islower()) # False
print (n.isupper()) # False
print (n.isspace()) # False
print (n.istitle()) # True
print (n.isprintable()) # True
print (n.isidentifier()) # True
print (n.isascii()) # True
print (n.isnumeric()) # False
print (n.isdecimal()) # False