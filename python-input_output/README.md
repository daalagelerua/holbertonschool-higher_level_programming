# Python - Input/Output

Let’s dive into **Python Input/Output (I/O)**, which is how Python interacts with the outside world, such as reading from or writing to files, taking user input, and displaying output.

## Standard Input and Output :

### Output: `print()`

The `print()` function is used to display output to the console.

<ins>**Example**</ins>:

```python
print("Hello, World!")  # Output: Hello, World!
print(42)               # Output: 42
print("The answer is", 42)  # Output: The answer is 42
```

**Customazing Output**:

* `sep`: Sspecifies the separator between arguments (default is a space).
* `end`: Specifies the end character (default is a new line).

```python
print("Python", "is", "awesome", sep="-", end="!\n")
# Output: Python-is-awesome!
```

### Input: `input()`

The `input()` function is used to take user input from the console. It always t=returns the inputs as a string.

<ins>**Example**</ins>:

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Type Casting**:

Convert the input to a different data type if needed.

```python
age = int(input("Enter your age: "))
print("You will be", age + 10, "in 10 years.")
```

## File Input/Output :

### Opening a File

Use the `open()` function to open a file. It returns a file object.

**Syntax**:

```python
file = open('filename', 'mode')
```

**Common Modes**:

* "`r`": Read mode (default).
* ``w``: Write mode (overwrites existing content).
* ``a``: Append mode (adds to the end of the file).
* ``b``: Binary mode (e.g., ``rb`` or ``wb``).
* ``x``: Exclusive creation (fails if the file exists).

### Reading from a File

* 