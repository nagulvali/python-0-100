

# Python Strings
- Strings in python are surrounded by either single quotation marks, or double quotation marks.

```python
print("Hello")
print('Hello')
```

- You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
```python
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
```

- Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
```python
a = "Hello"
print(a)
```

- You can assign a multiline string to a variable by using three quotes:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

- Or three single quotes:
```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

## Strings are Arrays
- Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
- However, Python does not have a character data type, a single character is simply a string with a length of 1.
- Square brackets can be used to access elements of the string.

```python
a = "Hello, World!"
print(a[1])
```

- Since strings are arrays, we can loop through the characters in a string, with a for loop.
```python
for x in "banana":
  print(x)
```

- To get the length of a string, use the len() function.
```python
a = "Hello, World!"
print(len(a))
```

- To check if a certain phrase or character is present in a string, we can use the keyword in.
```python
txt = "The best things in life are free!"
print("free" in txt)
```

- Use it in an if statement:
```python
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
```

- To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```

- Use it in an if statement:
```python
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```

## Slicing
- You can return a range of characters by using the slice syntax.
- Specify the start index and the end index, separated by a colon, to return a part of the string.
```python
b = "Hello, World!"
print(b[2:5])
```

- Get the characters from the start to position 5 (not included)
```python
b = "Hello, World!"
print(b[:5])
```

- Get the characters from position 2, and all the way to the end
```python
b = "Hello, World!"
print(b[2:])
```

- Use negative indexes to start the slice from the end of the string:
```python
b = "Hello, World!"
print(b[-5:-2])
```


## Concatentation
- To concatenate, or combine, two strings you can use the + operator.
- Merge variable a with variable b into variable c:
```python
a = "Hello"
b = "World"
c = a + b
print(c)
```

- To add a space between them, add a " ":
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```

## String Formatting
- We can combine strings and numbers by using f-strings or the format() method!
- F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
- To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
```python
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```

- A placeholder can contain variables, operations, functions, and modifiers to format the value.
- A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
```python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```
- A placeholder can contain Python code, like math operations:
```python
txt = f"The price is {20 * 59} dollars"
print(txt)
```

## Escape Characters
- To insert characters that are illegal in a string, use an escape character.
- An escape character is a backslash \ followed by the character you want to insert.
- An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
```python
txt = "We are the so-called \"Vikings\" from the north."
```
- Other escape characters used in Python:

| Escape Sequence | Description         |
|-----------------|:--------------------|
| \'              | Single Quote        |
| \\              | Backslash           |
| \n              | New Line            |
| \r              | Carriage Return     |
| \t              | Tab                 |
| \b              | Backspace           |
| \f              | Form Feed           |
| \ooo            | Octal value         |
| \xhh            | Hex value           |


## String Methods

### `capitalize()`
```python
text = "hello world"
print(text.capitalize())  # Hello world
```

### `casefold()`
```python
text = "HELLO"
print(text.casefold())  # hello
```

### `center()`
```python
text = "Python"
print(text.center(10, "-"))  # --Python--
```

### `count()`
```python
text = "banana"
print(text.count("a"))  # 3
```

### `encode()`
```python
text = "hello"
print(text.encode())  # b'hello'
```

### `endswith()`
```python
text = "filename.txt"
print(text.endswith(".txt"))  # True
```

### `expandtabs()`
```python
text = "name\tage"
print(text.expandtabs(4))  # name    age
```

### `find()`
```python
text = "hello world"
print(text.find("world"))  # 6
```

### `format()`
```python
print("My name is {}.".format("Nagul"))  # My name is Nagul.
```

### `format_map()`
```python
data = {"name": "Vali"}
print("My name is {name}".format_map(data))  # My name is Vali
```

### `index()`
```python
text = "hello"
print(text.index("e"))  # 1
```

### `isalnum()`
```python
text = "abc123"
print(text.isalnum())  # True
```

### `isalpha()`
```python
text = "hello"
print(text.isalpha())  # True
```

### `isascii()`
```python
text = "hello123"
print(text.isascii())  # True
```

### `isdecimal()`
```python
text = "123"
print(text.isdecimal())  # True
```

### `isdigit()`
```python
text = "1234"
print(text.isdigit())  # True
```

### `isidentifier()`
```python
text = "var_name"
print(text.isidentifier())  # True
```

### `islower()`
```python
text = "hello"
print(text.islower())  # True
```

### `isnumeric()`
```python
text = "123"
print(text.isnumeric())  # True
```

### `isprintable()`
```python
text = "hello\n"
print(text.isprintable())  # False
```

### `isspace()`
```python
text = "   "
print(text.isspace())  # True
```

### `istitle()`
```python
text = "Hello World"
print(text.istitle())  # True
```

### `isupper()`
```python
text = "HELLO"
print(text.isupper())  # True
```

### `join()`
```python
words = ["Hello", "World"]
print(" ".join(words))  # Hello World
```

### `ljust()`
```python
text = "Hi"
print(text.ljust(5, "."))  # Hi...
```

### `lower()`
```python
text = "HELLO"
print(text.lower())  # hello
```

### `lstrip()`
```python
text = "   hello"
print(text.lstrip())  # "hello"
```

### `maketrans()` + `translate()`
```python
table = str.maketrans("ae", "12")
text = "apple"
print(text.translate(table))  # 1ppl2
```

### `partition()`
```python
text = "user@example.com"
print(text.partition("@"))  # ('user', '@', 'example.com')
```

### `replace()`
```python
text = "banana"
print(text.replace("a", "o"))  # bonono
```

### `rfind()`
```python
text = "hello hello"
print(text.rfind("hello"))  # 6
```

### `rindex()`
```python
text = "hello hello"
print(text.rindex("hello"))  # 6
```

### `rjust()`
```python
text = "Hi"
print(text.rjust(5, "."))  # ...Hi
```

### `rpartition()`
```python
text = "a=b=c"
print(text.rpartition("="))  # ('a=b', '=', 'c')
```

### `rsplit()`
```python
text = "a,b,c"
print(text.rsplit(",", 1))  # ['a,b', 'c']
```

### `rstrip()`
```python
text = "hello   "
print(text.rstrip())  # "hello"
```

### `split()`
```python
text = "a,b,c"
print(text.split(","))  # ['a', 'b', 'c']
```

### `splitlines()`
```python
text = "line1\nline2"
print(text.splitlines())  # ['line1', 'line2']
```

### `startswith()`
```python
text = "Hello"
print(text.startswith("He"))  # True
```

### `strip()`
```python
text = "  hello  "
print(text.strip())  # "hello"
```

### `swapcase()`
```python
text = "Hello"
print(text.swapcase())  # hELLO
```

### `title()`
```python
text = "hello world"
print(text.title())  # Hello World
```

### `upper()`
```python
text = "hello"
print(text.upper())  # HELLO
```

### `zfill()`
```python
text = "42"
print(text.zfill(5))  # 00042
```














