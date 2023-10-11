# Learning Objectives

## What is Object-Oriented Programming
A way to structure code where data and functionality are combined inside something called an object, which are created by a class. Each object can have data and behaviour associated with it.

## “first-class everything”

### First-class Functions
Functions can be treated like variables i.e. pass them as arguments to other functions, and return them from other functions.

### First-class Objects
Objects can be created and manipulated at runtime. They can be created, assigned to variables, passed as arguments, and returned from functions.

### First-class Modules:
In Python, modules are code organised into reusable units. They can be imported, assigned to variables, and generally used like any other object.

### First-class classes
Classes can also be created, modified, and used dynamically.

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
Everyting is an object - integers, lists, dictionaries, functions, etc. 

They can also represent real-world objects and concepts. E.g. `Cat` can be a class with individual cats as objects created from that class.

Objects can store data using variables (aka fields) that *belong* to the object. They can also have functionality by using functions (methods) that *belong* to a class.

**Note:** Fields and methods are collectively known as attributes and are different to variables and functions (which are not dependent on objects/classes).

Instance is an object that belongs to a class. It has its own unique set of attributes and can perform actions using methods defined in teh class.

## What is the difference between a class and an object or instance
A class is like a blueprint/template. Instances is the tangible result created in the class based on the blueprint. Classes define what instances of a certain type should look like, behave. Instances will perform actions defined by the class.

Instances is a type of object. Everything is referred to as an object in Python.

## What is an attribute
An attribute is a variable that belongs to an object (instance of a class) or the class itself (a class attribute).

It stores data as a simple value, such as an integer, string, list, or any other data type.

Accessing an attribute is straightforward, using dot notation e.g. `object.attribute`.

Attributes do not involve any special behavior, validation, or methods for getting or setting their values. They are accessed directly.

## What are and how to use public, protected and private attributes
Attributes in a class have different levels of visibility.

### Public
They are accessible from anywhere, both inside and outside the class.

```
class Dora:
	def __init__(self):
	self.public_attribute == smol

cat = Dora()
print(cat.public_attribute)
```

### Protected
This is a naming convention with a single leading underscore: `_protected_attribute`. It means it is not considered public but can still be accessed in the same way.

```
class Dora:
	def __init__(self):
	self._protected_attribute == smol

cat = Dora()
print(cat._protected_attribute)
```

### Private
Also a naming convention with a double leading underscore: `__private_attribute` to indicate it should not be accessed directly from outside the class. Python will modify the name by addinf the class name as a prefix to make it more challenging to access outside of the class, but it's not a strict access control.

```
class Dora:
	def __init__(self):
	self._private_attribute == smol

cat = Dora()
print(cat._Dora__private_attribute)
```

## What is self
`Self` is the conventional name of a special variable that represents the instance of a class. It is used inside methods of a class to access and refer to the instance's attributes and methods. it allos classes to maintain individual state and behaviour for each of their instances.

### Initialising Attributes
In the constructor method, `self` is used to set the intiial attributes for an instance.

```
class Dora:
	def __init__(self, attribute):
		self.attribute = attribute # sets an instance attribute
```

### Accessing Instance Attributes
`self` is used to access instance-specific attributes and methods within class methods.

```
class Dora:
	def __init__(self, attribute):
		self.attribute = attribute
		
	def print_attribute(self):
		print(self.attribute) # accessing the instance attribute
```

### Calling Instance Methods
`self` is also used to call methods on the instance from within the class.

```
class Dora:
	def __init__(self, attribute):
		self.attribute = attribute
		
	def print_attribute(self):
		print(self.attribute)
	
	def modify_attribute(self, new_value):
		self.attribute = new_value # calls an instance method
```

## What is a method
**Methods** define the behaviour or action of objects. They are used to perform actions or operations on the object's attributes. E.g. `loaf` method migh change the state of the `shape` attribute of a `Cat` object.

```
class Cat:
	def __init__(self, name):
		self.name = name
		
	def meow(self):
		print(f"{self.name} meows!")

# creating an instance of the class "Cat"
my_cat = Cat("Dora")

# calling the "meow" method on an object
my_cat.meow()
# or Cat().meow()
```

Output:

```
Dora meows!
```

`meow` takes no parameters but still has `self` in the function definition.

## What is the special `__init__` method and how to use it

It is a special method that is automatically called when an instance of a class is created. It is used to initialise the attributes of properties of the object, ensuring they have appropriate initial values.

### Definition of __init__

```
class Cat:
    def __init__(self, name, size):
        self.name = name #param value assigned to object attributes
        self.size = size

```

There are now two different variables called 'name' but there are no issues because the dotted notation self.name means that there is something called "name" that is part of the object called "self", and the other name is a local variable. Since the code is explicitly indicate which name is being referred to, there is no confusion.

### Creating Instances
To create an object from the class, call the class name as if it were a function and pass the required parameters.

```
cat_name = Cat("Dora", "smol")
```

The `__init__` method will be automatically called with `self` referring to the new instance.

```
class Cat:
    def __init__(self, name, size):
        self.name = name
        self.size = size

# Creating objects of the "Cat" class
my_cat = Cat("Dora", "smol")

# Accessing attributes of the objects
print(my_cat.name)  # Output: "Dora"
print(my_cat.breed)  # Output: "smol"
```

## What is Data Abstraction, Data Encapsulation, and Information Hiding
They focus on managing the complexity and organisation of data and behaviour in a program.

### Data Abstraction
Data abstraction is a concept that simplifies complex reality by modeling classes based on the essential attributes and behaviors of objects.

It's like looking at a car and only paying attention to the things that matter, like its color and how it moves, and not about what's inside the engine.

### Data Encapsulation

Data encapsulation is the bundling of attributes and the methods that operate on that data into a single unit known as a class.

It enforces access restrictions on attributes and methods to control their visibility and accessibility from outside the class.

Encapsulation helps in maintaining data integrity and prevents unauthorized access and modification.

### Information Hiding

Information hiding ensures that the internal workings of a class are not visible or directly accessible from outside, protecting the integrity of the class's data.

Information hiding is achieved through access modifiers and naming conventions.


## What is a property
A property is a special attribute that is accessed and modified through methods known as getters and setters.

It allows behavior to be customised when reading or writing to the attribute, adding logic, validation, or custom actions.

Accessing a property appears like accessing an attribute but is backed by methods for getting and setting the value.

Properties are defined using the `@property` decorator for the getter method and `@<property_name>.setter` for the setter method.

## What is the difference between an attribute and a property in Python
The difference is how they are accessed and how the property can include validation logic (verify data is accurate, consistent and safe for processing) when setting the value.

Properties provide more control and flexibility.

## What is the Pythonic way to write getters and setters in Python
They are defined as methods but are accessed like attributes.

```
class Circle:
    def __init__(self, radius):
        self.radius_attribute = radius

    @property
    def radius_property(self):
        return self.radius_attribute

    @radius_property.setter
    def radius_property(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.radius_attribute = value

# Creating an object and using attribute and property
circle = Circle(5)
print(circle.radius_attribute)  # Accessing attribute
circle.radius_attribute = 7     # Modifying attribute
print(circle.radius_attribute)  # Updated attribute value

print(circle.radius_property)  # Accessing property
circle.radius_property = 7     # Modifying property
print(circle.radius_property)  # Updated property value

```

## How to dynamically create arbitrary new attributes for existing instances of a class
By simply assigning values to new attribute names. Python allows new attributes to be added at runtime. This is helpful for customisation and flexibility.

```
class MyClass:
    def __init__(self, initial_value):
        self.initial_attribute = initial_value

# Create an instance of MyClass
obj = MyClass(42)

# Dynamically create new attributes for the object
obj.new_attribute1 = "Hello"
obj.new_attribute2 = [1, 2, 3]

# Access the new attributes
print(obj.new_attribute1)  # Output: "Hello"
print(obj.new_attribute2)  # Output: [1, 2, 3]

```

## How to bind attributes to object and classes

### Binding Attributes to Objects (Instances)

   To bind an attribute to a specific instance of a class, use the dot notation and assign a value to it.

   ```
   class MyClass:
       def __init__(self, initial_value):
           self.instance_attribute = initial_value

   # Creating an instance of MyClass
   obj = MyClass(42)

   # Binding an attribute to the object
   obj.dynamic_attribute = "Hello"

   # Accessing attributes
   print(obj.instance_attribute)  # Output: 42
   print(obj.dynamic_attribute)   # Output: "Hello"
   ```

### Binding Attributes to Classes

Binding attributes to a class makes the attribute accessible for all instances of that class.

   ```
   class MyClass:
       class_attribute = "Class-level attribute"

   # Creating instances of MyClass
   obj1 = MyClass()
   obj2 = MyClass()

   # Accessing the class attribute from instances
   print(obj1.class_attribute)  # Output: "Class-level attribute"
   print(obj2.class_attribute)  # Output: "Class-level attribute"
   ```

## What is the `__dict__` of a class and/or instance of a class and what does it contain

The __dict__ attribute is a dictionary that stores the attributes (including methods) of a class or an instance of a class. It allows access and manipulation to the attributes as key-value pairs. The content of the __dict__ depends on whether it's accessed on a class or an instance.

Cass attributes and methods can be accessed directly using the dot notation (e.g., `MyClass.class_attribute` or `obj.instance_attribute`). 

### __dict__ of a Class:

It provides a dictionary containing the class attributes and methods. Class attributes are attributes defined at the class level, and class methods are functions defined within the class. 

```
class MyClass:
    class_attribute = "Class-level attribute"
    def class_method(self):
        pass

# Accessing the __dict__ of the class
class_dict = MyClass.__dict__

# Displaying the class's attributes and methods
for key, value in class_dict.items():
    print(key, value)
```

### __dict__ of an Instance:

 These attributes are specific to that instance and do not include class attributes.

```
class MyClass:
    def __init__(self, value):
        self.instance_attribute = value

# Creating an instance and accessing its __dict__
obj = MyClass("Instance-level attribute")
instance_dict = obj.__dict__

# Displaying the instance's attributes
for key, value in instance_dict.items():
    print(key, value)
```

## How does Python find the attributes of an object or class

Attribute access is a process that relies on a specific order to find attributes. It involves checking multiple namespaces or scopes.

### Instance Attributes
When an attribute is accessed on an object (e.g., `obj.attribute`), Python first looks for the attribute within the instance's namespace (the `__dict__` of the object).

If the attribute is found in the instance's namespace, it's returned.

### Class Attributes
If the attribute is not found in the instance's namespace, Python looks for it in the class's namespace (the `__dict__` of the class).

If the attribute is found in the class's namespace, it's returned.

This is why class attributes can be accessed using an instance (e.g., `obj.class_attribute`).

### Base Classes
If the attribute is not found in the class's namespace, Python will look in the namespaces of any base classes in the class's inheritance hierarchy.

The search continues up the inheritance chain until the attribute is found or until there are no more base classes.

### Global Namespace and Built-in Namespace
If the attribute is not found in any of the above namespaces, Python will search in the global namespace (if in a script or module) and finally in the built-in namespace (for Python's built-in functions and objects).

If the attribute is not found in these namespaces, Python raises an `AttributeError`.**

```
class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"

# Create an object of MyClass
obj = MyClass()

# Attribute access
print(obj.instance_attribute)     # Found in instance's namespace
print(obj.class_attribute)        # Found in class's namespace
print(MyClass.class_attribute)    # Found in class's namespace
print(obj.undefined_attribute)    # Not found, raises AttributeError
```

## How to use the getattr function

The `getattr` function is used to dynamically access and retrieve attributes of an object.

```
getattr(object, attribute_name, default)
```

- object from which you want to get the attribute.
- attribute_name as a string.
- an optional default value to return if the attribute does not exist. The function can also provide a default value.

```
class MyClass:
    def __init__(self):
        self.name = "John"
        self.age = 30

# Creating an instance of MyClass
obj = MyClass()

# Using getattr to access attributes
name = getattr(obj, "name")
age = getattr(obj, "age")

print(name)  # Output: "John"
print(age)   # Output: 30
```

`getattr(obj, "name")` retrieves the "name" attribute from the `obj` instance, and `getattr(obj, "age")` retrieves the "age" attribute.

```
# Using getattr with a default value
city = getattr(obj, "city", "Unknown")

print(city)  # Output: "Unknown" (because "city" attribute does not exist)
```

The `getattr` function is useful when attributes need to be accessed dynamically, based on user input or configuration settings. It allows the attributes to be accessed without explicitly knowing their names at coding time.
