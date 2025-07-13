# Code:
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

# Result:
# <class 'NoneType'>
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>


# Notes:
# - classes are blueprints to create multiple object instances
# - class can be created using class keyword
# - Camel case is standard practice to follow to create classes in python
class BigObject:
    pass

print(type(BigObject))

# Result
# <class 'type'>
# - The above code gives result `type` because it is plain class not object

obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()

print(type(obj1))
print(type(obj2))
print(type(obj3))

# Result:
# <class '__main__.BigObject'>
# <class '__main__.BigObject'>
# <class '__main__.BigObject'>

# We will understand about __main__ later, here object type is BigObject class type