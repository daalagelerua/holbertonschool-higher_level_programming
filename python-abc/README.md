# Python OOP - Abtract Class, Interface, Subclassing

<ins>**Introduction**</ins>:

Welcome to this set of exercises aimed at honing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through these exercises, you will delve into abstract classes, interfaces, duck typing, and subclassing standard base classes among other crucial OOP concepts. By the end of these exercises, you should be proficient in employing OOP principles to design, implement, and test Python programs.

<ins>**Learning Objectives**</ins>:

## Abstracts Classes :

An **abstract class** is a class which cannot be instantiated directly.
It serves as a template for other classes. It defines common methods (an interface) that derived classes must implement.

**Why Use It ?**: To ensure that certain methods are mandatory in child classes.

<ins>**Example**</ins>:

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def make_sound(self):  # Abstract method
        pass

class Dog(Animal):
    def make_sound(self):  # Mandatory implementation
        print("Woof!")

dog = Dog()
dog.make_sound()  # Outputs "Woof!"
```

## Interfaces and Duck Typing :

An **interface** is a contract that defines what a class should do, but not how it should do it; in Python, there is no `interface` keyword like in other languges (Java, C#), but abstract classes or conventions are used instead.

**Duck Typing**: In Python, we rely on an object's behavior rather than its type.
If an object has a `make_sound` method, it can be used as an animal, regardless of its class.

<ins>**Example**</ins>:

```python
class Duck:
    def make_sound(self):
        print("Quack!")

def make_it_speak(animal):
    animal.make_sound()

dog = Dog()
duck = Duck()

make_it_speak(dog)   # Outputs "Woof!"
make_it_speak(duck)  # Outputs "Quack!"
```

## Subclassing Standard Base Classes :

You ca create custom classes by inheriting from base classes like `list`,`dict` or `int`.
This allows you to add specialized behaviors.

<ins>**Example**</ins>:

```python
class MyList(list):  # Inherits from the list class
    def add_and_show(self, element):
        self.append(element)
        print(f"Element added: {element}")

my_list = MyList()
my_list.add_and_show(42)  # Outputs "Element added: 42"
```

## Method Overriding :

**Method overriding** allows a child class to provide a different implementation of a method already defined in the parent class.

<isn>**Example**</ins>:

```python
class Animal:
    def make_sound(self):
        print("Unknown sound")

class Cat(Animal):
    def make_sound(self):  # Method overriding
        print("Meow!")

cat = Cat()
cat.make_sound()  # Outputs "Meow!"
```

## Multiple Inheritance :

**Multiple inheritance** allows a class to inherit from multiple parent classes.
This can be useful for conbining functionalities, but you need to be careful about name conflicts.

<ins>**Example**</ins>:

```python
class Flyer:
    def fly(self):
        print("I'm flying!")

class Swimmer:
    def swim(self):
        print("I'm swimming!")

class Duck(Flyer, Swimmer):  # Multiple inheritance
    pass

duck = Duck()
duck.fly()  # Outputs "I'm flying!"
duck.swim()  # Outputs "I'm swimming!"
```

## Mixins :

A **Mixin** is a class designed to add functionality to other classes through multiple inheritance.
Unlike a regular class, a mixin is not meant to be used on its own.

<ins>**Example**</ins>:

```python
class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class MyClass(LoggerMixin):
    def do_something(self):
        self.log("Something was done")

obj = MyClass()
obj.do_something()  # Outputs "Log: Something was done"
```

***Summary***

- **Abstract Classes**: Define templates with mandatory methods.
- **Interfaces and Duck Typing**: Focus on behavior rather than type.
- **Subclassing**: Extend base classes for custom behaviors.
- **Method Overriding**: Redefine methods in child classes.
- **Multiple Inheritance**: Combine functionalities from multiple classes.
- **Mixins**: Add reusable functionality through inheritance.
