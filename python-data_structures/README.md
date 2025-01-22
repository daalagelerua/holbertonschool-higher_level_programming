# Python - Data Strctures: Lists, Tuples

## What are lists and how to use them ? :
**Lists** are ordered, mutable collections of items in Python. They can contain elements of different types, including other lists. Lists are defined using square brackets `[]`.

**How to use them**:
```python
# Creating a list
my_list = [1, 2, 3, "apple", "banana"]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[1] = "orange"
print(my_list)  # Output: [1, "orange", 3, "apple", "banana"]

# Adding elements
my_list.append("cherry")
print(my_list)  # Output: [1, "orange", 3, "apple", "banana", "cherry"]

# Removing elements
my_list.remove("apple")
print(my_list)  # Output: [1, "orange", 3, "banana", "cherry"]
```

## What are the differences and similarities between strings and lists ? :

<ins>**Similarities**</ins>:

- Both are sequences, meaning they are ordered collections of elements.
- Both support indexing and slicing.
- Both can be iterated over using loops.

<ins>**Differences**</ins>:

- **Mutability**: Lists are mutable (can be changed), while strings are immutable (cannot be changed).
- **Content**: Lists can contain elements of different types, while strings contain only characters.
- **Methods**: Lists have methods like append(), remove(), and pop(), while strings have methods like upper(), lower(), and replace().

## What are the most common methods of lists and how to use them ? :

<ins>**Common list methods**</ins>:

* `append(x)`: Adds an element x to the end of the list.
```python
my_list.append("grape")
```
* `extend(iterable)`: Adds all elements from an iterable to the list.
```python
my_list.extend(["kiwi", "mango"])
```
* `insert(i, x)`: Inserts element x at index i.
```python
my_list.insert(1, "pear")
```
* `remove(x)`: Removes the first occurrence of element x.
```python
my_list.remove("banana")
```
* `pop([i])`: Removes and returns the element at index i (or the last element if i is not specified).
```python
my_list.pop(2)
```
* `index(x)`: Returns the index of the first occurrence of element x.
```python
index = my_list.index("orange")
```
* `count(x)`: Returns the number of times element x appears in the list.
```python
count = my_list.count("cherry")
```
* `sort()`: Sorts the list in place.
```python
my_list.sort()
```
* `reverse()`: Reverses the list in place.
```python
my_list.reverse()
```

## How to use lists as stacks and queues ? :

**As a stack** (Last-In, First-Out):
```python
stack = []
stack.append("a")  # Push
stack.append("b")
print(stack.pop())  # Pop, Output: "b"
```
**As a queue** (First-In, First-Out):
```python
from collections import deque
queue = deque(["a", "b"])
queue.append("c")  # Enqueue
print(queue.popleft())  # Dequeue, Output: "a"
```

## What are list comprehensions and how to use them ? :

**List comprehensions** provide a concise way to create lists. They consist of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses.
```python
# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```
## What are tuples and how to use them ? :
**Tuples** are ordered, immutable collections of items. They are defined using parentheses `()`.
```python
# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements
print(my_tuple[0])  # Output: 1

# Tuples are immutable
# my_tuple[1] = "orange"  # This would raise a TypeError
```
## When to use tuples versus lists ? :

<ins>**Use tuples**</ins> when:

* You need an immutable sequence.
* You want to ensure that the data cannot be changed (e.g., for dictionary keys).
* You are dealing with a collection of items that should not be modified.

<ins>**Use lists**</ins> when:

* You need a mutable sequence.
* You want to add, remove, or modify elements.

## What is a sequence ? :

A **sequence** is an ordered collection of items. In Python, sequences include lists, tuples, strings, and ranges. Sequences support indexing, slicing, and iteration.

## What is tuple packing ? :
**Tuple packing** is the process of creating a tuple by assigning a sequence of values to a single variable.
```python
my_tuple = 1, 2, 3  # Tuple packing
print(my_tuple)  # Output: (1, 2, 3)
```
## What is sequence unpacking ? :
**Sequence unpacking** is the process of assigning the elements of a sequence to multiple variables.
```python
a, b, c = my_tuple  # Sequence unpacking
print(a, b, c)  # Output: 1 2 3
```
## What is the del statement and how to use it ? :
The `del` statement is used to delete objects, such as variables, list elements, or slices.
```python
# Deleting a variable
x = 10
del x
# print(x)  # This would raise a NameError

# Deleting list elements
my_list = [1, 2, 3, 4, 5]
del my_list[1]  # Deletes the element at index 1
print(my_list)  # Output: [1, 3, 4, 5]

# Deleting a slice
del my_list[1:3]
print(my_list)  # Output: [1, 5]
```
