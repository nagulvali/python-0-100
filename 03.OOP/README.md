# OOP (Object Oriented Programming)
- OOP stands for Object-Oriented Programming, a programming paradigm based on the concept of “objects”, which bundle data (attributes) and behavior (methods).
- Python is an object-oriented language, which means everything in Python is an object, including functions, classes, and even data types.
- class
  - A blueprint for creating objects.
  - Defined using the class keyword.
  ```
  class Car:
      pass
  ```
  
- object (Instance)
  - A real-world entity created from a class.
  ```
  my_car = Car()
  ```

- Constructor (__init__ method)
  - nitializes the object’s state. Called automatically when an object is created.
  ```
  def __init__(self, brand):
      self.brand = brand
  ```

- Attributes (Properties/Variables)
  - Data stored inside an object.
  ```
  self.brand = brand
  ```

- Methods
  - Functions defined inside a class that operate on object data.
  ```
  def drive(self):
      print(f"{self.brand} is driving")
  ```

- self keyword
  - Refers to the current object instance. Used to access attributes and methods.


## Four Pillars of OOP
- Encapsulation 
  - Hiding internal details and exposing only what is necessary. 
  - Done using private/protected/public attributes. 
  - Example: _protected, __private 
- Abstraction 
  - Showing only essential features and hiding complexities.
  - Often implemented using abstract classes or interfaces (via abc module). 
- Inheritance 
  - One class inherits properties and methods from another. 
  - Promotes code reuse.
  ```
  class ElectricCar(Car):
      pass
  ```
- Polymorphism
  - Same method behaves differently depending on the object.
  - Implemented via method overriding or duck typing.

## Benefits
- Code reusability
- Better structure and organization
- Easier to debug and maintain
- Models real-world systems effectively

## Concepts