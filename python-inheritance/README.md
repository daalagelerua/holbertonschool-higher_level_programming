# Python - Inheritance 

**Inheritance** is a fundamental concept in **object-oriented programming (OOP)** that allows a class (called a **subclass** or **child class**) to **inherit** attributes and methods from another class (called a **superclass**, **base class**, or **parent class**). Inheritance promotes **code reusability** and enables the creation of a hierarchical relationship between classes.

## Key Concepts of Inheritance :

1. ***Reusability***:

Instead of rewriting the same code, you can define common attributes and methods in a superclass and reuse them in subclasses.

2. ***Extensibility***:

Subclasses can extend or modify the behavior of the superclass by adding new attributes or methods or overriding existing ones.

3. ***Hierarchy***:

Inheritance creates a parent-child relationship between classes, forming a hierarchy.

4. ***Polymorphism***:

Objects of different subclasses can be treated as objects of the superclass, enabling flexibility in code design.

## What is a superclass, baseclass, or parentclass ?

A **superclass** (also called **baseclass** or **parentclass**) is a class that is inherited by another class (called a **subclass**). It provides attributes and methods that the subclass can use or override.

<ins>**Example**</ins>:

```python
class Animal:  # Superclass
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Subclass
    pass
```

## What is a subclass ?

A **subclass** is a class that inherits from a superclass. It can use or override the attributes and methods of the superclass and can also define its own.

<ins>**Example**</ins>:

```python
class Dog(Animal):  # Dog is a subclass of Animal
    def bark(self):
        print("Woof!")
```

## How to list all attributes and methods of a class or instance ?

- Use the `dir()` function to list all attributes and methods of a class or instance.

- Alternatively, use `.__dict__` to list instance-specific attributes.

<ins>**Example**</ins>:

```python
class MyClass:
    def __init__(self):
        self.x = 10
    def my_method(self):
        pass

obj = MyClass()
print(dir(MyClass))  # Lists all attributes and methods of the class
print(dir(obj))      # Lists all attributes and methods of the instance
print(obj.__dict__)  # Lists instance-specific attributes
```

## When can an instance have new attributes ?

An instance can have new attributes **dynamically** assigned at any time, even outside the class definition.

<ins>**Example**</ins>:

```python
class MyClass:
    pass

obj = MyClass()
obj.new_attribute = 42  # Dynamically adding a new attribute
print(obj.new_attribute)
```

## How to inherit a class from another ?

Use the syntax `Class Subclass(Superclass):` to inherit from a superclass.

<ins>**Example**</ins>:

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    pass
```

## How to define a class with multiple base classes ?

Use multiple inherithance by listing multiple base classes in the class definition: `class Subclass(base1, base2, ...):`.

<ins>**Example**</ins>:

```python
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):  # Inherits from both A and B
    pass
```

## What is the default class every class inherits from ?

In Python, every class implicitly inherits from the `object` class, which is the root of the class hierarchy.

<ins>**Example**</ins>:

```python
class MyClass:
    pass

print(issubclass(MyClass, object))  # True
```

## How to override a method or attribute inherited from the base class ?

Define a method or attribute with the same name in the subclass to override the one from the superclass.

<ins>**Example**</ins>:

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        print("Woof!")
```

## Whiche attributes or methods are available by heritage to subclass ?

- All **public** attributes and methods (those not prefixed with `_` or `__`) of the superclass are **available** to the subclasses.

- **Private** attributes (prefixed with `__`) are name-mangled and **not directly accessible**. 

<ins>**Example**</ins>:

```python
class Animal:
    def __init__(self):
        self.public_attr = 10
        self.__private_attr = 20

    def public_method(self):
        print("Public method")

    def __private_method(self):
        print("Private method")

class Dog(Animal):
    def access_parent(self):
        print(self.public_attr)  # Accessible
        self.public_method()     # Accessible
        # print(self.__private_attr)  # Not accessible
        # self.__private_method()     # Not accessible
```

## What is the purpose of inheritance ?

- **Code Reusability**: Avoid duplicating code by inheriting common functionality.
- **Extensibility**: Extend or modify behavior of existing classes.
- **Polymorphism**: Allow objects of different classes to be treated as objects of a common superclass.

## What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions ?

- `isinstance(object, classinfo)`:
Checks if an object is an instance of a class or a tuple of classes.

<ins>**Example**</ins>:

```python
obj = Dog()
print(isinstance(obj, Dog))  # True
print(isinstance(obj, Animal))  # True
```

- `issubclass(object, classinfo)`:
Checks if a class is a subclass of another class or a tuple of classes.

<ins>**Example**</ins>:

```python
print(issubclass(Dog, Animal))  # True
```

- `type(object)`:
Returns the type of an object.

<ins>**Example**</ins>:

```python
print(type(obj))  # <class '__main__.Dog'>
```

- `super()`:
Used to call a method from the superclass in the cotext of the subclass.

<ins>**Example**</ins>:

```python
class Dog(Animal):
    def speak(self):
        super().speak()  # Calls Animal's speak method
        print("Woof!")
```

## Summary :

Inheritance is a powerful OOP concept that allows you to:

* Reuse code by inheriting attributes and methods from a superclass.

* Extend or modify the behavior of existing classes.

* Create hierarchical relationships between classes.

*It is a key feature for writing clean, modular, and maintainable code.*
