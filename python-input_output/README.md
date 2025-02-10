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

* `'r'`: Read mode (default).
* `'w'`: Write mode (overwrites existing content).
* `'a'`: Append mode (adds to the end of the file).
* `'b'`: Binary mode (e.g., `'rb'` or `'wb'`).
* `'x'`: Exclusive creation (fails if the file exists).

### Reading from a File

* `read()`: Reads the entire file content.
* `readline()`: Reads one line at a time.
* `readlines()`: Reads all lines into a list.

<ins>**Example**</ins>:

```python
with open('example.txt', 'r') as file:
    content = file.read()  # Read the entire file
    print(content)
```

### Writing to a File

* `write()`: Writes a string to the file.
* `writelines()`: Writes a list of strings to the file.

<ins>**Example**</ins>:

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")
```

### Appending to a File 

Use the `'a'` mode to append to a file without overwriting it's content.

<ins>**Example**</ins>:

```python
with open('example.txt', 'a') as file:
    file.write("\nThis is an appended line.")
```

### Binary Files

For binary files (e.g., images, videos), use the `'b'` mode.

<ins>**Example**</ins>

```python
# Reading a binary file
with open('image.png', 'rb') as file:
    binary_data = file.read()

# Writing to a binary file
with open('copy.png', 'wb') as file:
    file.write(binary_data)
```

### File Cursor Manipulation

When you open a file, Python maintains a **cursor** (or pointer) that keeps track of the current position in the file. This cursor moves as you read or write data.

You can control the cursor's position using the following methods:

* `seek(offset)`: Moves the file cursor to a specific position (in bytes).
* `tell()`: Returns the current position of the file cursor (in bytes).

<ins>**Example**</ins>:

```python
with open('example.txt', 'r') as file:
    file.seek(10)  # Move cursor to the 10th byte
    print(file.read(5))  # Read the next 5 bytes
    print("Current position:", file.tell())  # Output: 15
```

### Using the `with` Statement

The `with` statement ensures that the file is automatically closed when the block is exited, even if an exception occurs.

<ins>**Example**</ins>:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

### Handling Exceptions in File I/O

Always handle exceptions when working with files to avoid crashes.

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")
```

## Working with JSON

### What is JSON ?

JSON (JavaScript Object Notation) is a lightweight data interchange format. It is easy for humans to read and write, and easy for machines to parse and generate.

<ins>**Example**</ins>:

```python
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

### Serialization and Deserialization

* **Serialization**: Converting a python object (e.g., dictionary, list) into a JSON sting.
* **Deserialization**: Converting a JSON string back into a python object.

<ins>**Example**</ins>:

```python
import json

# Serialization
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data, indent=4)  # Convert to JSON string
print(json_string)

# Deserialization
data = json.loads(json_string)  # Convert JSON string to Python object
print(data)
```

### Reading and Writing JSON Files

**Writing to a JSON File**:

```python
import json

data = {"name": "John", "age": 30, "city": "New York"}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Write data to JSON file
```

**Reading from a JSON File**:

```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)  # Load data from JSON file
    print(data)
```

## Working with CSV Files

### What are CSV Files ?

CSV (Comma-Separated Values) files are used to store tabular data (e.g., spreadsheets) in plain text. Each line in a CSV file represents a row, and columns are separated by a delimiter (usually a comma).

### Reading a CSV File

Use the `csv.reader` object to read a CSV file.

<ins>**Example**</ins>:

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### Writing to a CSV File

Use the `csv.writer` object to write to a CSV file.

<ins>**Example**</Ins>:

```python
import csv

data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"]
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

## Command-Line Arguments

### Accessing Command-Line Parameters

Use the `sys.argv` list from the `sys` module to access command-line arguments.

<ins>**Example**</ins>:

```python
import sys

# Example command: python script.py arg1 arg2
script_name = sys.argv[0]  # Name of the script
first_arg = sys.argv[1]    # First argument
second_arg = sys.argv[2]   # Second argument

print(f"Script: {script_name}")
print(f"First argument: {first_arg}")
print(f"Second argument: {second_arg}")
```

**Output**:

```python
Script: script.py
First argument: arg1
Second argument: arg2
```

***Summary***

* Use `print()` for output and `input()` for user input.
* Use `open()` to work with files, and always close them using `with`.
* Use `json` for JSON files and `csv` for CSV files.
* Handle exceptions to make your code robust.
* Use `sys.argv` to access command-line arguments.