# Python Built-in Data Types

- Text: str
- Numeric: int, float, complex
- Sequence: list, tuple, range
- Mapping: dict
- Set: set, frozenset
- Boolean: bool
- Binary: bytes, bytearray, memoryview
- NoneType: None

## Type Checking

```python
# Check type of a variable
type_variable = 42
print(type(type_variable))  # Output: <class 'int'>
```

## Setting Data Types
- In Python, the data type is set when you assign a value to a variable:

```python
# str
name = "Alice"
# int
age = 30
# float
height = 5.7
# complex
complex_number = 1 + 2j
# list
fruits = ["apple", "banana", "cherry"]
# tuple
coordinates = (10.0, 20.0)
# dict
person = {"name": "Alice", "age": 30}
# set
unique_numbers = {1, 2, 3, 4}
# frozenset
unique_frozen_numbers = frozenset([1, 2, 3, 4])
# bool
is_active = True
# bytes
data_bytes = b"Hello"
# bytearray
data_bytearray = bytearray(b"Hello")
# memoryview
data_memoryview = memoryview(b"Hello")
# NoneType
nothing = None
```

- If you want to specify the data type, you can use the following constructor functions:
```python
# str
name = str("Alice")
id = str(42)
# int
age = int(30)
# float
height = float(5.7)
# complex
complex_number = complex(1, 2)
# list
fruits = list(["apple", "banana", "cherry"])
# tuple
coordinates = tuple((10.0, 20.0))
# dict
person = dict(name="Alice", age=30)
# set
unique_numbers = set([1, 2, 3, 4])
# frozenset
unique_frozen_numbers = frozenset([1, 2, 3, 4])
# bool
is_active = bool(True)
# bytes
data_bytes = bytes("Hello", "utf-8")
# bytearray
data_bytearray = bytearray("Hello", "utf-8")
# memoryview
data_memoryview = memoryview(bytes("Hello", "utf-8"))
# NoneType
nothing = None
```

## More Information
- [01.Numbers](./01.Numbers)
- [02.Strings](./02.Strings)
- [03.Lists](./03.Lists)
- [04.Tuples](./04.Tuples)
- [05.Sets](./05.Sets)
- [06.Dictionaries](./06.Dictionaries)
- [07.Booleans](./07.Booleans)
- [08.Binary Types](./08.Binaries)
- [09.NoneType](./09.None)


