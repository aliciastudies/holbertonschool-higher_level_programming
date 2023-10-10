

# Learning Objectives

## What is Object-Oriented Programming
A way to structure code where data and functionality are combined inside something called an object.


## “first-class everything”

## What is a class

A template for creating objects. It defines the atrributes (data) and methods that objects of that class will have. 

```
class Cat:
	pass # an empty block
	
c = Cat()
print(c)

```
Output:

```
<__main__.Cat object at 0xffffa76d5e80>
```

`Cat` can have attributes like `colour`, and `gender`, and methods like `meow` and `loaf`.

## What is an object and an instance
Everyting is an object. They can represent real-world objects and concepts. E.g. `Cat` can be a class with individual cats as objects created from that class.

Objects can store data using variables (aka fields) that *belong* to the object. They can also have functionality by using functions (methods) that *belong* to a class.

**Note:** Fields and methods are collectively known as attributes and are different to variables and functions (which are not dependent on objects/classes).

## What is the difference between a class and an object or instance

## What is an attribute
**Fields** are the properties of an object. They store the state or characteristics of an object. They can be accessed and modified using dot notation. E.g. `my_cat.colour` changes the colour of the cat.

- instance variables belong to each instance/object
- class variables belong to the class itself

## What are and how to use public, protected and private attributes

## What is self
Class methods must have an extra first name added to the beginning of the parameter list. You do not have to give a value for the parameter when the method is called. Python will provide it. This variable refers to the object itself and by convention is given the same `self`.

## What is a method
**Methods** define the behaviour of the objects. They are used to perform actions or operations on the object's attributes. E.g. `loaf` method migh change the state of the `shape` attribute of a `Cat` object.

```
class Cat:
	def meow(self):
		print("Meoooow!")
	
c = Cat()
c.meow()
# or Cat().meow()
```
Output:

```
Meoooow!
```
`meow` takes no parameters but still has `self` in the function definition.

## What is the special `__init__` method and how to use it

It runs as soon as an object of a class is created. It is useful to pass initial values to the object.

```
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print('Hai, my name is', self.name)

c = Cat('Dora')
c.meow()

```
The __init__ method is defined as taking a parameter name and self. A new field is created, also called name.

There are now two different variables called 'name' but there are no issues because the dotted notation self.name means that there is something called "name" that is part of the object called "self", and the other name is a local variable. Since the code is explicitly indicate which name is being referred to, there is no confusion.

When creating new instance c, of the class Cat, the class name is used, followed by the arguments in the parentheses: c = Cat('Dora').

The __init__ method is specialy because it is not explicitly called.

The self.name field can now be used in the meow method.

## What is Data Abstraction, Data Encapsulation, and Information Hiding

## What is a property

## What is the difference between an attribute and a property in Python

## What is the Pythonic way to write getters and setters in Python

## How to dynamically create arbitrary new attributes for existing instances of a class

## How to bind attributes to object and classes

## What is the `__dict__` of a class and/or instance of a class and what does it contain

## How does Python find the attributes of an object or class

## How to use the getattr function