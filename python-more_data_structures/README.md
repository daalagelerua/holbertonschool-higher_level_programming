# Python - More Data Structures: Set, Dictionary

## What are Sets and How to Use Them :

A set is an unordered collection of unique elements. It is defined using curly braces `{}` or the `set()` function.

 <ins>**Example:**</ins>
```python
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}
```
<ins>**Key Characteristics:**</ins>
- **Unordered**: Elements are not stored in any specific order.
- **Unique**: No duplicate element are allowed.
- **Mutable**: You can add or remove elements.

## Most Common Methods of Sets :

Here are some common set methods:

***Add an Element:***
```python
my_set.add(5)  # Adds 5 to the set
```

***Remove an Element:***
```python
my_set.remove(3)  # Removes 3 from the set (raises an error if not found)
my_set.discard(3)  # Removes 3 if it exists (no error if not found)
```

***Union of Sets:***
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5}
```

***Intersection of Sets:***
```python
intersection_set = set1.intersection(set2)  # Output: {3}
```

***Difference of Sets:***
```python
difference_set = set1.difference(set2)  # Output: {1, 2}
```

***Check Subset:***
```python
is_subset = set1.issubset(set2)  # Returns True or False
```

## When to use Sets vs Lists :

<ins>**Use Sets:**</ins>
- When you need to store unique elements.
- When you need fast membership testing (e.g., checking if an element exists).
- When order doesn't matter.

<ins>**Use Lists:**</ins>
- When you need to maintain order.
- When you need to allow duplicate elements.
- When you need indexed access to elements.

## How to Iterate over a Set :

You can iterate over a set using a for loop:
```python
my_set = {1, 2, 3, 4}
for item in my_set:
    print(item)
```

## What are Dictionaries and How to Use Them :

A **dictionary** is an unordered collection of **key-value** pairs. It is defined using curly braces `{}` with `key:value` pairs.

<ins>**Example:**</ins>
```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Output: Alice
```

<ins>**Key Characteristics:**</ins>

- **Unordered**: Keys are not stored in any specific order.
- **Mutable**: You can add, remove, or modify key-value pairs.
- **Keys must be unique**: No duplicate keys are allowed.

## When to Use Dictionaries vs Lists or Sets :

<ins>**Use Dictionaries:**</ins>
- When you need to store data as key-value pairs.
- When you need fast lookups by key.

<ins>**Use Lists:**</ins>
- When you need ordered, indexed data.

<ins>**Use Sets:**</ins>
- When you need to store unique elements and perform set operations.

## What is a Key in a Dictionary :

A **key** is a unique identifier used to access a value in a dictionary. Keys must be immutable (e.g, strings, numbers, tuples).

<ins>**Examples:**</ins>
```python
my_dict = {"name": "Alice", "age": 25}
# "name" and "age" are keys.
```

## How to Iterate over a Dictionary :

You can iterate over *keys*, *values* or *key-values* pairs:

***Iterate Over Keys:***
```python
for key in my_dict:
    print(key)
```
***Iterate Over Values:***
```python
for value in my_dict.values():
    print(value)
```
***Iterate Over Key-Value Pairs:***
```python
for key, value in my_dict.items():
    print(key, value)
```

## What is a Lambda Function :

A **lambda function** is a small anonymous function defined using the `lambda` keyword. It can have any number of arguments but only one expression.

<ins>**Examples:**</ins>
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

## What are the `map`, `reduce`, and `filter` Functions :

These are higher-order Functions used for functional programming.

`map`:
Applies a function to all items in an iterable.
```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
```
`filter`:
Filters items based on a condition.
```python
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]
```
`reduce`:
Applies a function cumulatively to items in an iterable (requires `functools`
```python
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 10
```



