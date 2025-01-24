# Python - Exceptions

## What’s the difference between errors and exceptions ? :

- **Errors** are typically issues that are serious and often unrecoverable, 
such as syntax errors, out-of-memory errors, or system crashes. 
They usually indicate problems with the code itself or 
the environment in which the code is running.

- **Exceptions** are events that occur during the execution of a program that
disrupt the normal flow of instructions. 
They are often recoverable and can be handled by the program. 
Exceptions are typically used to handle unexpected conditions, 
such as invalid input, file not found, or network issues.

## What are the exceptions and how to use them ? :

- **Exceptions** are objects that represent an error or an unexpected event that
occurs during the execution of a program. In many programming languages,
exceptions are instances of a class that inherits from a base exception class.

- **How to use them**: You can use exceptions to handle errors gracefully
by catching them and taking appropriate action. This is typically done using `try`,
  `except`, and `finally` blocks in languages like Python.

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero!")
finally:
    # Code that runs no matter what
    print("Execution complete.")
```

## When do we need to use exceptions ? :

- **Use exceptions** when you anticipate that a certain operation might fail due to reasons
beyond your control, such as:
  * File I/O operations (e.g., file not found, permission denied).
  * Network operations (e.g., connection timeout, server not responding).
  * Invalid user input.
  * Resource availability issues (e.g., memory allocation failure).
- **Exceptions** should be used for **exceptional conditions**, situations that are not part of
the normal flow of the program.

## How to correctly handle an exception ? :

***Correctly handling an exception*** involves:
1. **Catching the exception**: Use a `try` block to wrap the code that might raise an exception.
2. **Handling the excepton**: Use an `except` block to define how to respond to the exception.
3. **Optional cleanup**: Use a `finally` block to ensure that the resources are released or
cleanup actions are performed, regardless of whether an exception occured.
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()  # Ensure the file is closed
```

## What's the purpose of catching exceptions ? :

***The purpose of catching exceptions*** is to:
* **Prevent the program from crashing**: By handling exceptions, you can ensure that your program
continues to run even if an error occurs.
* **Provide meaningfull feedback**: You can inform the user or log the error in a way that helps
diagnose the issue.
* **Recover from errors**: In some cases, you can take corrective action and retry the operation.

## How to raise a built-in exception ? :

**Raising a built-in exception** is done using the `raise` keyword in languages like Python.
You can raise an exception when you detect an error condition in your code.
```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)  # Output: Cannot divide by zero!
```
 
## When do we need to implement a clean-up action after an exception ? :

**Implement a clean-up action** when you need to ensure that resources are properly released
or that certains actions are taken regardless of whether an exception occured.
This is typically done in a `finally` block or using context managers like `with`.
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()  # Ensure the file is closed even if an exception occurs
```

**Context managers** automatically handled cleanup:
```python
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
```
In this case, the file is automatically closed when th `with` block is exited, 
even if an exception occurs.
