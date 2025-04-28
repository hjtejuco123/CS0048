# Python Conditional and Looping Statements"

---

# 1. Conditional Statements

## 1.1 What are Conditional Statements?
- Control the flow of the program based on conditions.
- Executes different blocks depending on whether a condition is `True` or `False`.

> Non-zero/Non-null = `True`  |  Zero/Null = `False`

---

## 1.2 Basic `if` Statement

```python
num = 5
if num > 0:
    print("Positive number")
```

---

## 1.3 `if-else` Statement

```python
num = -3
if num >= 0:
    print("Positive number")
else:
    print("Negative number")
```

---

## 1.4 `if-elif-else` Statement

```python
num = 0
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

---

## 1.5 Nested `if` Statement

```python
num = 15
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```

---

## 1.6 Single Line `if` Statement

```python
a = 10
b = 5
if a > b: print("a is greater than b")
```

---

# 2. Loops in Python

## 2.1 What are Loops?
- Execute a block of code multiple times while a condition is true.

---

## 2.2 `while` Loop

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

---

### `while` Loop with `else`

```python
count = 0
while count < 3:
    print("Inside loop:", count)
    count += 1
else:
    print("Loop finished!")
```

---

## 2.3 `for` Loop

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

### Using `range()` in `for` Loop

```python
for i in range(3):
    print(i)
```

```python
for i in range(1, 10, 2):
    print(i)
```

---

### `for` Loop with `else`

```python
for number in range(3):
    print(number)
else:
    print("Loop done!")
```

---

## 2.4 Nested Loops

```python
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```

---

# 3. Loop Control Statements

## 3.1 `break` Statement

```python
for letter in "Python":
    if letter == "h":
        break
    print(letter)
```

---

## 3.2 `continue` Statement

```python
for letter in "Python":
    if letter == "h":
        continue
    print(letter)
```

---

## 3.3 `pass` Statement

```python
for letter in "Python":
    if letter == "h":
        pass
    print(letter)
```

```python
def future_function():
    pass
```

---

# 🌟 Summary Table

| Concept | Purpose | Example |
|:-------|:--------|:--------|
| `if` | Execute code if condition is True | `if x > 0:` |
| `if-else` | Execute based on True/False | `if x>0 else ...` |
| `elif` | Check multiple conditions | `if x>0 elif x==0 else` |
| `while` loop | Repeat while condition is True | `while x < 10:` |
| `for` loop | Traverse a sequence | `for i in range(5):` |
| `break` | Exit loop immediately | `if i == 3: break` |
| `continue` | Skip current iteration | `if i == 3: continue` |
| `pass` | Empty placeholder | `pass` |

---
