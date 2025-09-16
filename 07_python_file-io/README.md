# 📂 File Handling in Python

File handling is an important part of programming that allows you to **create, read, update, and delete files**. Python provides built-in functions and methods to work with files efficiently.

---

## ✨ Why File Handling?

- To store data permanently.
- To read/write logs, configurations, and user data.
- To handle large datasets without keeping them all in memory.

---

## 📌 Opening a File

In Python, you use the `open()` function:

```python
file = open("filename.txt", "mode")
```

## 📌 File Modes in Python

| Mode   | Description                                                                    |
| ------ | ------------------------------------------------------------------------------ |
| `'r'`  | Read (default). File must exist, otherwise error.                              |
| `'w'`  | Write. Creates a new file or overwrites an existing file.                      |
| `'a'`  | Append. Creates a new file if it does not exist, otherwise appends at the end. |
| `'x'`  | Exclusive Create. Fails if the file already exists.                            |
| `'b'`  | Binary mode (used for non-text files like images, videos).                     |
| `'t'`  | Text mode (default, used for text files).                                      |
| `'r+'` | Read and Write. File must exist, starts from the beginning.                    |
| `'w+'` | Write and Read. Overwrites existing file or creates a new one.                 |
| `'a+'` | Append and Read. Creates new file if not exists, appends otherwise.            |

# 📖 Reading Files

## 1. Read entire file:

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

## 2. Read line by line:

```python

with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

## 3. Read specific number of characters:

```python

with open("data.txt", "r") as f:
    content = f.read(10)  # reads first 10 characters
    print(content)
```

## 4. Readlines (list of lines):

```python

with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

# ✍ Writing to Files

## 1. Write (overwrite file):

```python

with open("data.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This will overwrite the file.")
```

## 2. Append (add data without deleting old content):

```python

with open("data.txt", "a") as f:
    f.write("\nNew line added at the end.")
```

# 🔄 File Pointer Operations

```python

Using seek() and tell():
with open("data.txt", "r") as f:
    print(f.tell())   # current pointer position
    print(f.read(5))  # read 5 chars
    f.seek(0)         # move pointer to start
    print(f.read(10))
```

# 📂 Working with Binary Files

```python

with open("image.jpg", "rb") as f:
    data = f.read()

with open("copy.jpg", "wb") as f:
    f.write(data)

```

# ✅ Check if File Exists

```python

import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")
```

# ❌ Deleting Files

```python

import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
else:
    print("File not found")
```

# 📂 Directory Operations

```python

import os

# Create folder
os.mkdir("my_folder")

# List files
print(os.listdir("."))

# Remove folder
os.rmdir("my_folder")

⚡ Exception Handling in File Handling
try:
    with open("unknown.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist!")

```

# 🔥 Best Practices

- Always use with open() (auto closes file).

- Handle exceptions with try-except.

- Use relative paths for portability.

- Keep file operations minimal to improve performance.

# 📝 Example Project – Count Words in File

```python
with open("data.txt", "r") as f:
    text = f.read()

words = text.split()
print("Total words:", len(words))
```

# 🎯 Interview Questions

- What are different file modes in Python?

- Difference between **read()**, **readline()**, and **readlines()?**

- Why is with **open()** better than **open()?**

- How to copy a binary file (like images or PDFs)?

- How do you handle file not found errors in Python?

# 🚀 Conclusion

- File handling is a core skill in Python. It allows us to persist data, process files, and build real-world applications like log systems, data analysis tools, and file-based storage systems.
