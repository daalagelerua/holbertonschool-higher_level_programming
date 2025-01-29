# Python - More Classes

## `.str()` and `repr()` :

Both `str()` and `repr()` are used to get string representations of an object, but they serve different purposes.

**`str()`**

- Called when you use `str(obj)`,`print(obj)`, or `f"{obj}"`
- Should return a **user-friendly** and **readable** string representation of the object.
- Defined using the `__str__` method in a class.

**`repr()`**

- Called when you use `repr(obj)`
- Should return an **unambiguous**, **developer-fiendly** string representation that could ideally be used to recreate the object.
- Defined using the `__repr__` methode in a class.
- If `__str__` is not defined, `str(obj)` falls back to using `__repr__`.

<ins>**Example**</ins>:

```python
class Square:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Square with size {self.size}"  # Readable for users

    def __repr__(self):
        return f"Square({self.size})"  # Unambiguous, for debugging

square = Square(4)
print(str(square))  # Output: Square with size 4
print(repr(square)) # Output: Square(4)
```

## `__del__`: The Destructor :

- `__del__` is called **when an object is about to be destroyed**.
- Useful for cleanup operations, like closing files or network connections.
- In practice, Python's garbage collector handles most cleanups, so `__del__` is rarely needed.

<ins>**Example**</ins>:

```python
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "w")
        print("File opened")

    def __del__(self):
        self.file.close()
        print("File closed")

fh = FileHandler("test.txt")
del fh  # Explicitly deleting the object
# Output:
# File opened
# File closed
```
⚠️ **Caution**: Relying on `__del__` is risky because the exact moment an object is destroyed is **not guaranted**

## `__doc__`: The Docstring :

- `__doc__` stores the **documentation string** (docstring) of a class, function, or module.
- Helps in understanding what a class or function does.
- Can be accessed using `obj.__doc__`.

<ins>**Example**</ins>:

```python
class Square:
    """This class represents a square with a given size."""
    
    def __init__(self, size):
        """Initialize a square with a given size."""
        self.size = size

print(Square.__doc__)   # Output: This class represents a square with a given size.
print(Square.__init__.__doc__)  # Output: Initialize a square with a given size.
```

> [!NOTE]
> Good documentation makes code easier to understand and maintain!

## Quick Summary

| Method     | Purpose                                                |
|------------|--------------------------------------------------------|
| `__str__`  | User-friendly string representation (`str(obj)`)       |
| `__repr__` | Developer-friendly, debug representation (`repr(obj)`) |
| `__del__`  | Destructor, called when an object is deleted           |
| `__doc__`  | Stores docstrings for documentation                    |
