# Python - Test-driven Development

## What's an Interactive Test :

An **interactive test** is a type of software test where the tester interacts with the system in real-time,
providing inputs and observing outputs to verify the correctness of the software. Unlike automated tests, which run without human intervention, interactive tests rquire manual onput and evaluation. These tests are often used for exploratory testing, usability testing, or when automated testing is not feasible.

## Why Tests Are Important :

Tests are crucial in software development for several reasons:

1. **Ensure Correctness**: Tests verify that the code behaves as expected and meets the requirements.
2. **Prevent Regressions**: They catch bugs introduced during code changes, ensuring existing functionality isn't broken.
3. **Improve Code Quality**: Writing tests encourages modular, maintainable, and well-structured code.
4. **Documentation**: Tests serve as living documentation, showing how the code is supposed to work.
5. **Facilitate Refactoring**: With a good test suite, developers can refactor code confidently.
6. **Save Time**: Automated tests reduce the need for manual testing, speeding up developement.

## How to Write Docstring to Create Tests :

Docstrings can be used to describe the purpose of a function or module and include examples that can be used as tests.
Many testing frameworks, like Python's `doctest`, can extract and run these examples directly from docstrings.

<ins>**Example**</ins>:

```python
def add(a, b):
    """
    Adds two numbers together.

    Examples:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```

To run these tests :

```python
python -m doctest my_module.py
```

## How to Write Documentation for Each Module and Function :

Good documentation helps others (and your future self) understand and use your code effectively. Here's how to document modules and functions:

1. **Module Documentation**:

- Describe the purpose of the module.
- List important classes, functions, and variables.
- Include usage examples if applicable.

<ins>**Example**</ins>:

```python
"""
This module provides mathematical operations like addition and subtraction.

Functions:
- add(a, b): Returns the sum of two numbers.
- subtract(a, b): Returns the difference between two numbers.
"""
```

2. **Function Documentation**:

- Describe what the function does.
- List parameters and their types.
- Describe the return value.
- Include examples or edge cases.

<ins>**Example**</ins>:

```python
def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The result of a - b.

    Examples:
    >>> subtract(5, 3)
    2
    >>> subtract(0, 5)
    -5
    """
    return a - b
```

## Basic Option Flags to Create Tests :

When running tests, many testing frameworks provide option flags to control test execution. Here are some common ones:

1. Verbose Output:
* `v` or `--verbose`: Shows detailed output for each test case.
* Example: `python -m unittest -v`

2. Run Specific Tests:
* `-k <pattern>`: Runs only tests that match the pattern.
* Example: `pytest -k "test_add"`

3. Stop on First Failure:
* `-x` or `--exitfirst`: Stops the test run after the first failure.
* Example: `pytest -x`

4. Coverage Report:
* `--cov`: Generates a coverage report (requires pytest-cov).
* Example: `pytest --cov=my_module`

5. Ignore Warnings:
* `-W ignore`: Suppresses warning messages during test execution.
* Example: `python -W ignore -m unittest`

## How to Find Edge Cases :

Edge cases are inputs or conditions that are at the extreme ends of the expected input domain. Finding them is critical for robust software. Here’s how to identify edge cases:

1. Boundary Values:
* Test the minimum and maximum allowed values.
* Example: For a function that accepts integers between 1 and 100, test 1, 100, 0, and 101.

2. Empty Inputs:
* Test with empty strings, lists, or other data structures.
* Example: `""`, `[]`, `{}`.

3. Null or None Inputs:
* Test how the function handles None or null values.

4. Unexpected Data Types:
* Test with invalid data types (e.g., passing a string to a function expecting an integer).

5. Extreme Values:
* Test with very large or very small numbers.
* Example: `float('inf')`, `-float('inf')`.

6. Concurrency Issues:
* Test how the function behaves under high load or concurrent access.

7. Real-World Scenarios:
* Think about how users might misuse the function or module.

<ins>**Example**</ins>:

```python
def divide(a, b):
    """
    Divides two numbers.

    Edge Cases:
    >>> divide(10, 0)  # Division by zero
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    >>> divide(0, 10)  # Numerator is zero
    0.0
    """
    return a / b
```