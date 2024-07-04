# Python Developer Coding Test

This repository contains solutions to a Python developer coding test, covering various programming problems.

## Problem Statements

### Problem 1: Reverse a String

**Description:** Write a function that reverses a given string.

**File:** `problemOne.py`

**Coding Structure:**
- Define a function that takes a string as input.
- Use slicing (`[::-1]`) to reverse the string.
- Return the reversed string.

### Problem 2: List Comprehensions

**Description:** Write a function that generates squares of even numbers from a list of integers.

**File:** `problemTwo.py`

**Coding Structure:**
- Define a function that takes a list of integers as input.
- Use list comprehensions to filter even numbers and compute their squares.
- Return a list of squared even numbers.

### Problem 3: File I/O

**Description:** Write a function that reads a text file and counts the number of words in it.

**File:** `problemThree.py`

**Coding Structure:**
- Define a function that takes a file name as input.
- Use `open()` with `with` statement to read the file.
- Split the file content into words using `split()`.
- Return the count of words.

### Problem 4: Dictionary Manipulation

**Description:** Write a function that sorts a dictionary by its values in ascending order.

**File:** `problemFour.py`

**Coding Structure:**
- Define a function that takes a dictionary as input.
- Use `sorted()` with a lambda function to sort the dictionary by values.
- Return the sorted dictionary.

### Problem 5: Bank Account Management

**Description:** Implement functions to manage bank accounts using file I/O.

**File:** `problemFive.py`

**Coding Structure:**
- Define a class `BankAccountManager` with methods for balance retrieval, deposit, withdrawal, and account updates.
- Use file I/O (`open()`, `write()`, `read()`) to store and retrieve account information.
- Handle exceptions for file operations and account management.

