# Loops in Python

Loops are used to execute a block of code repeatedly until a certain condition is met. Python provides `for` and `while` loops to perform repetitive tasks efficiently.

---

## 1. For Loop

The `for` loop is used to iterate over a sequence (like list, tuple, string) or a range of numbers.

**Syntax:**

```python
for variable in sequence:
    # code block
```

**Example:**

```python
for i in range(1, 6):
    print("Number:", i)
```

**Output:**

```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

---

## 2. While Loop

The `while` loop executes as long as a condition is true.

**Syntax:**

```python
while condition:
    # code block
```

**Example:**

```python
i = 1
while i <= 5:
    print("Number:", i)
    i += 1
```

**Output:**

```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

---

## 3. Nested Loops

A loop inside another loop is called a nested loop. Useful for iterating over multi-dimensional structures.

**Example:**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
```

**Output:**

```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3
```

---

## 4. Loop Control Statements

### `break`

Terminates the loop completely.

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

**Output:**

```
1
2
3
```

### `continue`

Skips the current iteration and continues with the next.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**

```
1
2
4
5
```

### `pass`

Does nothing, used as a placeholder.

```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

**Output:**

```
1
2
3
4
5
```

---

## Summary Table

| Loop Type   | Description                       | When to Use                  |
| ----------- | --------------------------------- | ---------------------------- |
| for loop    | Iterates over sequence or range   | Known number of iterations   |
| while loop  | Executes until condition is False | Unknown number of iterations |
| nested loop | Loop inside another loop          | Multi-dimensional iteration  |
| break       | Exit the loop                     | Stop loop based on condition |
| continue    | Skip current iteration            | Skip specific cases in loop  |
| pass        | Placeholder                       | No action, used as stub      |
