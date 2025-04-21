# CS0048
# Python Programming Tutorial
# By: Dr. Hadji J. Tejuco

![Python Logo](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

# 📘 Module 1: Introduction to Python Programming

> This module introduces students to Python, including its history, features, installation process, syntax, and basic programming concepts.

---

## 🎯 Learning Objectives

By the end of this module, students should be able to:

- Define Python.
- Identify key features of Python.
- List various applications of Python.
- Compare Python syntax to other programming languages.
- Explain the history and versions of Python.
- Install and set up Python.
- Understand Python basic syntax and identifiers.
- Use user input, variables, and data types.
- Identify and use comparison and logical operators.

---

## 🐍 What is Python?

Python is a **high-level**, **interpreted**, and **object-oriented** scripting language known for its readability and simplicity. It is commonly used in:

- Web development
- Software development
- Mathematics
- System scripting
- Data analysis and AI

---

## ✨ Key Features of Python

- Interpreted and Interactive
- Object-Oriented
- Beginner-Friendly
- Easy-to-learn syntax
- Extensive standard libraries
- Platform-independent
- Extendable with C/C++
- GUI Support
- Dynamic Typing
- Integrated with DBs and Web

---

## 🧠 Python Applications

- Web applications
- Workflow automation
- Database connectivity
- Big Data and mathematical operations
- Rapid prototyping and production

---

## 🕰️ History and Versions

- Developed by **Guido van Rossum** in the late 1980s.
- Influenced by languages like ABC, C, Modula-3, and SmallTalk.
- **Python 1.0** – 1994  
- **Python 2.0** – 2000 (last: 2.7.11)  
- **Python 3.0** – 2008 (not backward compatible, latest: 3.8.3+)

---

## ⚙️ Installing Python

Installers available for:

- **Windows**
- **Mac**
- **Linux**

Tools:
- Text Editors: Notepad
- IDEs: Thonny, PyCharm, VS Code

---

## 🔤 Python Syntax Overview

- Uses **indentation** for blocks (no `{}` or `;`)
- Case-sensitive
- Commands end with newline, not `;`

### Control Statements:

- `if`, `else`, `elif`
- `for`, `while`, `break`, `continue`
- `try`, `except`, `finally`, `raise`
- `class`, `def`, `with`, `pass`, `yield`

### Expressions:

- `+`, `-`, `*`, `/`, `//`, `**`
- `==`, `!=`, `<`, `>`, `<=`, `>=`
- `and`, `or`, `not`
- `is`, `in`
- `lambda`, `x if c else y`
- `@` (matrix multiplication)
- `:=` (walrus operator)

---

## ✍️ Identifiers and Variables

- Must start with a letter or `_`
- Can contain letters, digits, `_`
- Case-sensitive (`Age` ≠ `age`)
- Dynamically typed

# 🔁 Module 2: Conditional Statements and Loops in Python
> Learn how to make decisions and perform repetitive tasks in Python using conditional statements and loops.

---

## ✅ Topics Covered

### 🔹 Conditional Statements in Python
- What are Conditional Statements?
- Truthy and Falsy values in Python
- `if` statement
- `if-else` statement
- `if-elif-else` statement
- Nested `if` statements
- Single-line `if` statements

### 🔹 Loops in Python
- Sequential execution vs Repetition
- `while` loop
  - Syntax and flow
  - Use of `else` with `while`
- `for` loop
  - Iteration over a sequence
  - Using `range()` with `for`
  - Using `len()` with `for`
  - Use of `else` with `for`
- Nested Loops
- Using `end` in `print()` for formatting loop output

### 🔹 Loop Control Statements
- `break`: Exit a loop early
- `continue`: Skip current iteration
- `pass`: Placeholder statement in loops and functions

---

# 🔧 Module 3: Functions in Python

---

## 🎯 Learning Objectives

- Define Python functions.
- List and discuss the different types of functions.
- Write the syntax of a function.
- Demonstrate how to run a function in Python.
- Discuss the scope and lifetime of variables.

---

## ✅ Topics Covered

### 🔹 Introduction to Functions
- Purpose and benefits of using functions
- Code reusability and modularization

### 🔹 Types of Functions
- Built-in functions (e.g. `print()`, `help()`, `min()`)
- User-defined functions
- Anonymous functions (Lambda functions)

### 🔹 Defining Functions in Python
- `def` keyword
- Function name and parameters
- Docstrings
- Indentation and body
- `return` statement

### 🔹 Calling Functions
- Syntax for invoking functions
- Positional and keyword arguments

### 🔹 Scope and Lifetime of Variables
- Local variables
- Global variables
- Variable lifetime within function execution

### 🔹 Function Parameters
- Default arguments
- Keyword arguments
- Arbitrary arguments (`*args`)
- Rules on argument ordering

### 🔹 Recursive Functions
- Definition and use cases
- Base case and recursive step
- Pros and cons of recursion

### 🔹 Lambda Functions
- Syntax and structure
- When to use lambda functions
- Lambda with `map()` and `filter()`

### 🔹 Global, Local, and Nonlocal Variables
- `global` keyword usage
- `nonlocal` keyword usage
- Behavior of variable scope in nested functions

### 🔹 Modules in Python
- What are modules?
- Importing modules using:
  - `import module`
  - `import module as alias`
  - `from module import item`
  - `from module import *`
- Best practices in importing

### 🔹 Packages in Python
- Directory structure and `__init__.py`
- Organizing modules in packages
- Importing modules from packages using dot (`.`) notation

---
# 🧱 Module 4: Object-Oriented Programming (OOP) in Python

---

## 🎯 Learning Objectives

- Understand Object-Oriented Programming in Python
- Define and explain:
  - Class
  - Inheritance
  - Operator Overloading
- Apply OOP concepts effectively in Python

---

## ✅ Topics Covered

### 🔹 Introduction to OOP in Python
- What is Object-Oriented Programming?
- Advantages of OOP: DRY principle, reusability, modularity

### 🔹 Objects and Classes
- Understanding objects (attributes and behavior)
- Defining classes using `class` keyword
- Creating object instances
- `__init__()` method and constructors
- Accessing attributes and methods

### 🔹 Instance Methods and Class Attributes
- Defining methods inside classes
- `self` keyword
- Accessing and modifying attributes

### 🔹 Inheritance
- Base and derived classes
- Overriding methods
- Using `super()` to access parent class methods
- `isinstance()` and `issubclass()` checks

### 🔹 Multiple and Multilevel Inheritance
- Syntax and structure
- Inheriting from multiple base classes
- Creating deeper class hierarchies

### 🔹 Encapsulation
- Public vs. private attributes
- Name mangling using `_` and `__`
- Getters and setters

### 🔹 Polymorphism
- Method overriding
- Common interfaces for different classes

### 🔹 Special Methods and Operator Overloading
- Special methods like `__init__`, `__str__`, and `__add__`
- Making classes compatible with Python’s built-in operators
- Overloading arithmetic and comparison operators (`+`, `<`, etc.)

### 🔹 Object Lifetime and Garbage Collection
- Creating and deleting attributes and objects
- Understanding object references and automatic cleanup

---

# 🧮 Module 5: Data Types in Python

---

## 🎯 Learning Objectives

- List the different data types in Python.
- Define and describe:
  - List
  - Tuple
  - String
  - Set
  - Dictionary
- Apply data type concepts using Python syntax.

---

## ✅ Topics Covered

### 🔹 Core Data Types in Python
- Numbers
- List
- Tuple
- String
- Set
- Dictionary

---

## 🔢 Numbers
- Integer, Float, Complex types
- Type checking with `type()` and `isinstance()`
- Type conversion and coercion (`int()`, `float()`, `complex()`)
- Decimal and Fraction modules
- Floating-point limitations and precision control
- Mathematical operations using `math` and `random` modules

---

## 📝 Lists
- Definition and creation using `[]`
- Indexing, slicing, and negative indexing
- Mutability and item modification
- Adding: `append()`, `extend()`, `insert()`, `+`, `*`
- Removing: `del`, `remove()`, `pop()`, `clear()`
- List methods and `list.method()`
- List comprehension
- Membership testing and iteration with `for`

---

## 📦 Tuples
- Definition and creation using `()`
- Immutability vs lists
- Indexing and slicing
- Tuple methods
- Tuple membership testing and iteration
- Tuple advantages over lists

---

## 🔤 Strings
- Definition and creation with quotes (`'`, `"`, `'''`)
- Indexing, slicing, and immutability
- Escape sequences and raw strings
- String concatenation and repetition (`+`, `*`)
- Built-in string functions: `len()`, `enumerate()`
- String formatting: `format()`, `%`, and format specifiers
- String methods: `lower()`, `upper()`, `split()`, `join()`, `replace()`, etc.

---

## 🧮 Sets
- Definition using `{}` or `set()`
- Unordered and unique elements
- Adding: `add()`, `update()`
- Removing: `remove()`, `discard()`, `pop()`, `clear()`
- Set operations: union, intersection, difference, symmetric difference
- Built-in functions with sets: `all()`, `any()`, `max()`, `min()`, `sum()`
- `frozenset` — immutable set

---

## 🗂️ Dictionaries
- Definition using `{key: value}` syntax
- Accessing values with keys and `get()`
- Mutability: adding, updating, and deleting items
- Removal: `pop()`, `popitem()`, `del`, `clear()`
- Dictionary comprehension
- Built-in functions with dictionaries: `len()`, `sorted()`, etc.

---
# 🗂️ Module 6: Python Files and Exception Handling

---

## 🎯 Learning Objectives

- Understand the need for file handling in large applications.
- Learn to:
  - Open, read, write, and close files in Python.
  - Differentiate between text and binary files.
  - Handle file and directory operations using the `os` module.
  - Use exception handling to manage program errors.
- Apply file I/O and exception concepts in Python programming.

---

## ✅ Topics Covered

### 🔹 Introduction to File Handling
- Importance of files in data persistence
- Real-life file management analogy
- File operations: open, read, write, close
- File types:
  - Binary files (e.g., `.pdf`, `.jpg`, `.exe`)
  - Text files (e.g., `.txt`, `.csv`, `.py`)

---

### 🔹 File Operations in Python

#### `open()` Function
- Syntax and parameters (`file_name`, `mode`, `buffering`)
- Access modes: `'r'`, `'w'`, `'a'`, `'b'`, `'x'`, etc.

#### File Object Attributes
- `.name`, `.mode`, `.closed`, `.softspace`

#### `close()` Method
- Flushing and closing the file safely

#### Writing to Files
- `write()` method (no newline added)

#### Reading from Files
- `read()`, `readline()`, `readlines()`
- Reading partial or entire content

#### `tell()` and `seek()`
- Tracking and repositioning file pointer

---

### 🔹 File Management with `os` Module

#### File and Directory Handling
- `os.rename()` — rename files
- `os.remove()` — delete files
- `os.mkdir()` — create directories
- `os.chdir()` — change current directory
- `os.getcwd()` — get current directory
- `os.rmdir()` — remove directory

#### Utility Sources
- File object methods
- OS module file methods

---

### 🔹 Exception Handling in Python

#### What is an Exception?
- Errors disrupting normal program flow
- Types of built-in exceptions

#### `try-except` Block
- Catching specific exceptions
- Generic exception handling
- Multiple `except` blocks
- Optional `else` block (runs if no exception)

#### `finally` Block
- Always runs regardless of exception

#### Catching Exception with Arguments
- Exception argument object
- Using variables to retrieve error messages

---

### 🔹 Raising Exceptions
- `raise` keyword to manually trigger exceptions
- Syntax with custom messages
- `raise Exception("message")`

---

### 🔹 User-Defined Exceptions
- Creating custom exceptions with classes
- Inheriting from `Exception` or `RuntimeError`
- Raising and handling user-defined exceptions

---


