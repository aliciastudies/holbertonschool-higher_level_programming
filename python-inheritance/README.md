# Learning Objectives

## What is a superclass, baseclass or parentclass
They are a type of class that a subclass inherits from. It provides attributes and methods that the subclass can use.

## What is a subclass
It inherits attributes and methods from another class, known as its superclass or parentclass. The subclass can also add its own attributes and methods.

## How to list all attributes and methods of a class or instance
You can list all attributes and methods of a class using the `dir()`. `dir(instance)` will display all attributes and methods of the class `instance`.

## When can an instance have new attributes
An instance can have new attributes added at any time.

```
instance.new_attribute = value
```

## How to inherit class from another

```
class Subclass(Superclass):
```

## How to define a class with multiple base classes

```
class Subclass(BaseClass1, BaseClass2):
```

## What is the default class every class inherit from
Every class implicitly inherits from a default class called object. This provides some basic functionality to all classes.

## How to override a method or attribute inherited from the base class
Define a method or attribute with the same name in the subclass. This will replace the inherited one.

## Which attributes or methods are available by heritage to subclasses
All attributes and methods (unless private) from a base class are available to subclasses.

## What is the purpose of inheritance
To promote code reuse and organisation. It allows new classes to be created that will also incorporate the behavior of existing classes, while also allowing you to customise or extend that behaviour.

## What are, when and how to use isinstance, issubclass, type and super built-in functions
`isinstance(obj, class)` checks if `obj` is an instance of a specified class.

`issubclass(subclass, superclass)` checks if a class subclass is a subclass of superclass.

`type(obj)` returns the type of `obj`.

`super()` calls methods and accesses attributes from the superclass within a subclass.
