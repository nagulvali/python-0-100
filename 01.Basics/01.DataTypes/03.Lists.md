# Python Lists
- Lists are used to store multiple items in a single variable.
- Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
- Lists are created using square brackets:

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

- List items are ordered, changeable, and allow duplicate values.
  - When we say that lists are ordered, it means that the items have a defined order, and that order will not change. 
  - If you add new items to a list, the new items will be placed at the end of the list.
  - There are some list methods that will change the order, but in general: the order of the items will not change.
- List items are indexed, the first item has index [0], the second item has index [1] etc.
- The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
- Since lists are indexed, lists can have items with the same value
```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```
- To determine how many items a list has, use the len() function:
```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```

- List items can be of any data type:
```python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

- A list can contain different data types:
```python
list1 = ["abc", 34, True, 40, "male"]
```

- From Python's perspective, lists are defined as objects with the data type 'list':
```python
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #<class 'list'>
``` 

- It is also possible to use the list() constructor when creating a new list.
```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```

- There are four collection data types in the Python programming language:
  - **List** is a collection which is ordered and changeable. Allows duplicate members. 
  - **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members. 
  - **Set** is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
    - Set items are unchangeable, but you can remove and/or add items whenever you like.
  - **Dictionary** is a collection which is ordered and changeable. No duplicate members.
    - As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

- When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


## Accessing List Items
- List items are indexed and you can access them by referring to the index number:
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```

- Negative indexing means start from the end
  - `-1` refers to the last item, `-2` refers to the second last item etc.
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```

- Range of Indexes
  - You can specify a range of indexes by specifying where to start and where to end the range.
  - When specifying a range, the return value will be a new list with the specified items.
```python
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
```

- To determine if a specified item is present in a list use the in keyword:
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

## Changing List Items
- To change the value of a specific item, refer to the index number:
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```

- To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```

- If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
```python
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
```

- If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
```python
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
```

- To insert a new list item, without replacing any of the existing values, we can use the insert() method.
- The insert() method inserts an item at the specified index:
```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```

## Add/Remove List Items

## Loop List Items

## List Comprehension

## Sort List Items

## Copy List Items

## Join Lists

## List Methods

## Problems


