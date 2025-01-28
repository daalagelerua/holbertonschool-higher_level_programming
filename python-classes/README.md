# Python - Classes and Objects

## What is OOP :

**OOP (Object-Oriented Programming)** is a programming paradigm that organizes
software design around **objects** and **classes**. It emphasizes concepts like:

- **Encapsulation**:
Bundling data (attributes) and methods (functions) that operate on the data int a single unit (class).
- **Inheritance**:
Creating new classes (child classes) from existing ones (parent classes) to 
reuse and extend functionality.
- **Polymorphism**:
Allowing objects of different classes to be treated as objects of a common superclass.
- **Abstraction**:
Hiding complex implementation details and exposing only essential features.

*OOP makes code modular, reusable, and easier to maintain.*

## What is "first-class everything" :

In Python, **"first-class everything"** means that almost all entities (functions,
classes, modules, methods, etc) are trated as **objects**. This means:

- They can be assigned to variables.
- They can be passed as arguments to functions.
- They can be returned from functions.
- They can be stored in data structures like lists or dictionaries.

<ins>**Example**</ins>:

```python
def greet():
    return "Hello!"

# Assigning a function to a variable
my_function = greet
print(my_function())  # Output: Hello!
```

## What is a Class :

A **class** is a blueprint or template for creating objects. It defines:

- **Attributes**:
Variables that hold data.
- **Methods**:
Functions that define behavior.

<ins>**Example**</ins>:

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Attribute

    def bark(self):  # Method
        print(f"{self.name} says woof!")
```

## What is an Object and an Instance :

- An **object** is an instance of a class. It is a concrete entity created from the class blueprint.
- An **instance** is another term for an object. When you create an object, you are instantiating the class.

<ins>**Example**</ins>:

```python
my_dog = Dog("Buddy")  # my_dog is an instance/object of the Dog class
my_dog.bark()  # Output: Buddy says woof!
```

## Difference Between a Class and an Object/Instance :

- A **class** is a blueprint or template.
- An **object/instance** is a concrete entity created from the class.

<ins>**Example**</ins>:

* `Dog` is a class.
* `my_dog = Dog("Buddy")` creates an object/instance of the `Dog` class.

## What is an Attribute :

An **attribute** is a variable that belongs to an object or class. It holds data associated with the object or class.

<ins>**Example**</ins>:

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute

Dog.species = "Canine"  # Class attribute
```

## Public, Protected, and Private attributes :

- **Public**:
Accessible from anywhere. No special syntax.
- **Protected**:
Intended for internal use. Prefix with a single underscore (_). Not enforced by Python.
- **Private**:
Intended to be inaccessible outside the class. Prefix with double underscore (__). Name mangling is applied.

<ins>**Example**</ins>:

```python
class MyClass:
    def __init__(self):
        self.public = 10      # Public
        self._protected = 20  # Protected
        self.__private = 30   # Private

obj = MyClass()
print(obj.public)       # Works
print(obj._protected)   # Works (but discouraged)
print(obj.__private)    # Error (name mangling applied)
```

## What id `self` :

`self` is a reference to the current instance of the class. It is used to access attributes and methods of the instance within a class.

<ins>**Example**</ins>:

```python
class Dog:
    def __init__(self, name):
        self.name = name  # self refers to the instance
```

## What is a Method :

A **method** is a function defined within a class that operates on the instance (or class) data.

<ins>**Example**</ins>:

```python
class Dog:
    def bark(self):
        print("Woof!")
```

## What is the Special `__init__` Method :

The `__init__` method is a **constructor** in Python. It is automatically called when a new instance of a class is created. It is used to initialize instance attributes.

<ins>**Example**</ins>:

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

## Data Abstraction, Encapsulation, and Information Hiding :

- **Data Abstraction**:
Exposing only essential features while hiding implementation details.
- **Encapsulation**:
Bundling data methods into a single unit (class).
- **Information Hiding**:
Resticting access to certain attributes or methods (using private attributes).

## What is Property :

A **property** is a special attribute that allows controlled access to an instance attribute. It is defined using th `@property` decorator.

<ins>**Example**</ins>:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius
```

## Difference Between an Attribute and a Property :

- An **attribute** is a simple variable.
- A **property** is a method that behave like an attribute, allowing controlled access.

## Pythonic Way to Write Getters and Setters :

Use the `@property` decorator for getters and `@<property>.setter` for setters.

<ins>**Example**</ins>:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
```
 

## Dynamically Create Attributes :

You can add attributes to an instance dynamically using dot notation.

<ins>**Example**</ins>:

```python
class Dog:
    pass

my_dog = Dog()
my_dog.name = "Buddy"  # Dynamically added attribute
```


## Binding Attributes to Oblects and Classes :

- Attributes can be bound to instances or classes.
- Instance attributes are specific to the instance.
- Class attributes are shared accross all instances.

## What is `__dict__` :

`__dict__` is a dictonary containing the attributes of an object or class.

<ins>**Example**</ins>:

```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")
print(my_dog.__dict__)  # Output: {'name': 'Buddy'}
```

## How Python Finds Attributes :

Python uses the **attribute lookup order**:

1. Instance attributes.
2. Class attributes.
3. Parent class attributes (in case of inheritance).

## How to Use `getattr` :

`getattr` is a built-in function to retrieve an attribute from an object. It allows specifying a default value if the attribute doesn't exist.

<ins>**Example**</ins>:

```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")
print(getattr(my_dog, 'name'))  # Output: Buddy
print(getattr(my_dog, 'age', 5))  # Output: 5 (default value)
```
