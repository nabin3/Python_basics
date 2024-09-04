## Exceptions to Identation rules in python:
List can be wriiten in multiline because python knows until it doesn't find closing ']', a list don't ends. We can write instructions in multiline using '\' as 
it says current statement continues in next line.



## None value:
In Python, there is a value called None, which represents the absence of a value. The None value is the only value of the NoneType data type. Incase of missing return statement ```None``` returned implicitly.

## Keyword arguments:
Most arguments are identified by there position, but in case of optional arguments we use keyword argument.
```bash
>>> print('Hello', end='') # print() function puts newline in the end of the string but here we are asking it to put empty string after the string
```

## Augmented assignment operator:
```+=, *=, -=, /=``` are example of this type of operator.

## List:
List can contain multiple values. They can contain other lists also, so a hirearchical datastructure can be built. List is a sequence of values, the values are called items and we can store multiple type pf value in a list. The list also refferedas ```list value```. List maintain order for storing it's items, so we can access list items by indexes.

### Negative index:
Generally indexes start at 0 amd go upwards, but we can use negative integers as
indexes where -1 denotes last item in a list and -2 denotes second last item in 
the list and so on.

### Slices:
With slice we can create a new list from an existing list. It consists of list ne from where we want to create the new list, two integers one for begining(inclusive) of the new list and other for ending(exclusive) of new list and a colon **:** 
between those two integers. If first is ommited then 0 will use in that place and if last is ommitted then source list's length will be used.
```bash
>>> num = [2, 4, 6, 8, 10]
>>> num[1:3]
[4, 6]
>>> num[:5]
[2, 4, 6, 8, 10]
>>> num[2:]
[6, 8, 10]
```

### List Concatenation and Replication:
We can create a new list by concatenating two lists with **+** operator.
```bash
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
```
List can be replicted also by multiplying a list with an integer.
```bash
>>> ['x' , 'y', 'z'] * 3
['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']
```

### Working with lists
To store a group of similar values it is good to use a list.
```bash
cat_names = []                                                                                                                                                      while True:                                                                           print('Enter name of cat no.' + str(len(cat_names) + 1) + ' (or nothing to stop)')
    name = input()
    if name == '':
        break
    else:
        cat_names += [name]

print('Entered cat names are:')
for name in cat_names:
    print(name, end = ' ')

print()

```

### Del statement:
Del delete a list item if we give index of that item. And Every item's index after deleted item will be shif upwards by 1. We even delete a variable with del keyword, after that if we want to access that deleted cariable we will get ```NameError```
```bash
>>> animals = ['cat', 'bat', 'rat', 'elephant']
>>> del animal[2]
>>> animals
['cat', 'bat', 'elephant']
```

### in and not in:
with these we can determine if one item is present or not in a list. There expression evaluates to ```True``` or ```False```.
```bash
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyad']
True
>>> spams = ['hello', 'hi', 'howdy', 'heyad']
>>> 'cat' in spams
False
>>> 'cat' not in spams
True
>>> 'howdy' not in spams
False
>>>
```

### Multiple assignement trick:
This trich technical name is ```tuple unpacking```. In this technique we can assign multiple variables with values of a list in one line. But remind that it is must to have equal number of variables and list values, if not ```ValueError``` error will occur.
```bash
>>> cat = ['fat', 'gray', 'loud']
>>> size, color, disposition = cat
>>> print(size + ' ' + color + ' ' + disposition)
fat gray loud
>>> size, color, disposition, name = cat
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
>>> size, color = cat
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

### enumarate() function in list:
When we want index and item both we can use enumarate instead of range(len_of_list), this enumarate() function returns two value 1st is index and 2nd is item.
```bash
>>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders'] 
>>> for index, item in enumerate(supplies):
... print('Index ' + str(index) + ' in supplies is: ' + item) 

Index 0 in supplies is: pens 
Index 1 in supplies is: staplers 
Index 2 in supplies is: flamethrowers 
Index 3 in supplies is: binders
```

### random.choice() and random.shuffle() in list:
These two functions take one list as argument. ```random.choice(list_variable)``` return a randomly choiced item from the given list. It is the shortend version of 
```list_variable[random.randInt(0, len(list_variable)-1]```
Example:
```bash
>>> import random
>>> pets = ['Dog', 'Cat', 'Moose']
>>> random.choice(pets)
'Cat'
>>> random.choice(pets)
'Moose'
>>> random.choice(pets)
'Dog'
>>> random.choice(pets)
'Cat'
>>> random.choice(pets)
'Dog'
```
The ```random.shuffle()``` function will reorder the items in a list. This function modifies the list in place, rather than creating a new list.
example:
```bash
>>> people = ['Alice', 'Bob', 'Carol', 'David'] 
>>> random.shuffle(people) 
>>> people 
['Carol', 'David', 'Alice', 'Bob']
```

## Methods:
A method is the same thing as a function, except it is called on a value(object). For example, if a list were stored in ```spam```, you would call index() list method on that list like this: ```spam.index('hello')```

### Finding a value in a list with index() method:
This method takes a value as an argument, if that value exists then it will return the index of that value in the list and if the value doesn't exist in the list then 
```ValueError``` error will occur.
```bash
>>> spam = ['hello', 'hi', 'howdy', 'heyas'] 
>>> spam.index('hello') 
0 
>>> spam.index('heyas') 
3 
>>> spam.index('howdy howdy howdy') 
Traceback (most recent call last):
    File "<pyshell#31>", line 1, in <module>
        spam.index('howdy howdy howdy') 
ValueError: 'howdy howdy howdy' is not in list
```
When there are duplicates of the value in the list, the index of the first appearance is returned.
```bash
>>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka'] 
>>> spam.index('Pooka') 
1
```

### Adding  Values to List with append() and insert() method:
They does the same thing, but the difference is ```list_var.append(item)``` always add item at the end of the list where ```insert(index_where_to_be_insert, item)```
can add item in any specified index. These two methods mutate the(don't give a new list) list and they are also exclusive to list.
```bash
spams = ['hello', 'hi', 'howdy', 'heyad']
>>> spams.append('hola')
>>> spams
['hello', 'hi', 'howdy', 'heyad', 'hola']
>>> spams.insert(2, 'namaskaram')
>>> spams
['hello', 'hi', 'namaskaram', 'howdy', 'heyad', 'hola']
```

### Removing Values from the lists with the remove method:
When we know the index of the item we want to remove we can use ```del```, but when we know the item need to be removed but don't know it's index we use ```remove()```
method. This method takes an item which need to be deleted and mutate the list on which it is called. If this method has passed an item not present in the list, will 
give a ValueError error. And if the value passed to remove appears multiple time in calling list, then only first appearance will be deleted.
```bash
spams = ['hello', 'hi', 'namaskaram', 'howdy', 'heyad', 'hola']
>>> spams.remove('hi')
>>> spams
['hello', 'namaskaram', 'howdy', 'heyad', 'hola']
>>> spams.remove('pen')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

### sort() method:
This method sort a list of number values or a list of strings in place.
```bash
>>> num = [5, 7, 3, 6, 2, 1, 0]
>>> num.sort()
>>> num
[0, 1, 2, 3, 5, 6, 7]
```
If we use ```reverse``` keyword argument with value ```True``` then ```a_list.sort(reverse=True)``` will sort a list in reverse(decending) order.
```bash
>>> num = [3, 19, 4, 1, 11, 2, 5, 0]
>>> num.sort(reverse=True)
>>> num
[19, 11, 5, 4, 3, 2, 1, 0]
```
This method can't sort a list of both number vaues and strings because it doesn't know how to compare the items with each other.
```bash
>>> various = [7, 3, 8, 'hola', 'gola', 'cola']
>>> various.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
```
This method sort list in ```ASCIIbetical``` order.
```bash
>>> food = ['rice', 'Roasted Tomato', 'scrambled egg', 'Chicken Kasha']
>>> food.sort()
>>> food
['Chicken Kasha', 'Roasted Tomato', 'rice', 'scrambled egg']
```
If you pass keyword argument ```a_list.sort(key=str.lower)```, then sort() method will treat every letter in list as lower case letter, but don't modify anytging in list.
```bash
>>> food = ['rice', 'Roasted Tomato', 'scrambled egg', 'Chicken Kasha']
>>> food.sort(key=str.lower)
>>> food
['Chicken Kasha', 'rice', 'Roasted Tomato', 'scrambled egg']
```

### reverse():
When we want to reverse order of items in a list we use ```a_list.reverse()```    method. This also reverse the list in place.
```bash
>>> food
['Chicken Kasha', 'rice', 'Roasted Tomato', 'scrambled egg']
>>> food.reverse()
>>> food
['scrambled egg', 'Roasted Tomato', 'rice', 'Chicken Kasha']
```
```append(), extend(), remove(), reverse(), sort()``` they all mutate list i.e they are in place method.


## Sequence Data Types
Lists aren’t the only data types that represent ordered sequences of values.
For example, strings and lists are actually similar if you consider a string to be a “list” of single text characters. The Python sequence data types include lists,
strings, range objects returned by range(), and tuples. Many of the things you can do with lists can also be done with strings and other values of sequence types: index-ing; slicing; and using them with for loops, with len(), and with the in and not in operators.
    But list is **mutable** where string and tuple are **immutable**. We can create new string from slicing and concatenating.
```bash
>>> name = 'Zophie a cat' 
>>> newName = name[0:7] + 'the' + name[8:12] 
>>> name 
'Zophie a cat' 
>>> newName 
'Zophie the cat'


>>> name = 'Zophie a cat' 
>>> name[7] = 'the' 
Traceback (most recent call last):
    File "<pyshell#50>", line 1, in <module> 
        name[7] = 'the' 
TypeError: 'str' object does not support item assignment 

>>> eggs = [1, 2, 3]
>>> eggs = [4, 5, 6]
# The list value in eggs is not changing here, but a new list value is again ass
```

## Tuple:
Tuple items written inside parenthesis '()'. If tuple has only one item then put a ',' after that item otherwise python will think it just a value inside regular 
parenthesis.
```bash
>>> type(('hello',)) 
<class 'tuple'> 
>>> type(('hello')) 
<class 'str'>
```
As tuple is immutable, we can use tuple to tell anyone, reading our code that we don't want to change the sequence of items or modify them.
```bash
>>> eggs = ('hello', 42, 0.5)
>>> eggs[1] = 99 
Traceback (most recent call last):
    File "<pyshell#5>", line 1, in <module>
        eggs[1] = 99 
 TypeError: 'tuple' object does not support item assignment
```
Another advntage is as tuple's order and item won't change python will apply some optimazation here and for that reason program using tuple run faster than progrem using list.

## Converting Types with list() and tuple() functions:
Like str(), int() the list()  and tuple() will return list and tuple version of the values passed to them.
```bash
>>> tuple(['cat', 'dog', 5]) 
('cat', 'dog', 5) 
>>> list(('cat', 'dog', 5)) 
['cat', 'dog', 5]
```

## References:
```bash
>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42
```
First 42 is created in computer memory and then storeed the reference of that memory location in spam variable. Then copied the reference from spam to cheese.
Now created 100 somewhere in computer memory and assign that memory address's reference to spam, now spam indicates 100 where cheese still indicates 42. 

In case of list:
```bash
>>> num = [5, 6, 7]
# bam referencing same list value as num
>>> bam = num
# Creating list value [7, 8, 9] in computer memory and  assigning the reference of that memory locatioan
>>> bam = [7 ,8, 9]
# Reassigning the 1st indexed item in num referenced list value.
>>> num[1] = 10
# As bam references different list value then it havn't effected with reassogning num's 1st indexed item with 10 
>>> bam
[7, 8, 9]
# But num ofcourse effected
>>> num
[5, 10, 7]
# Now vam also referencing same list value as num
>>> vam = num
# Reassigning vam referenced list value's 2nd indexed item with 50
>>> vam[2] = 50
# As num referencing same list value as vam then the change with vm reflected in nam aso
>>> num
[5, 10, 50]
# vam ofcourse has updated
>>> vam
[5, 10, 50]
```
```id(value)``` function returns an unique value, this is the reference assigned to variables.
Python’s automatic garbage collector deletes any values not being referred to by any variables to free up memory.
When passing list or dictionaries in a function call there values don't copied instead their refrences copied. For this reason function call on list and dictionaries make mutation effect.

## copy() and deepcopy():
Passing list or dictiomary in function call deals with copy of reference not copy of vaue. So we get mutation behaviour in case of list and dictionary in function 
call. But when we don't want this mutational behaviour instead we want immutaional behaviour, we want to send copy of value of list or dictionary in function call 
instead of copy of referencesc. To do that we use copy() and deepcopy()(in case of
nested list or dictionary) function from **copy** module.
```bash
>>> import copy 
>>> spam = ['A', 'B', 'C', 'D'] 
>>> id(spam) 
44684232 
>>> cheese = copy.copy(spam) 
>>> id(cheese) # cheese is a different list with different identity.
44685832 
>>> cheese[1] = 42 
>>> spam ['A', 'B', 'C', 'D'] 
>>> cheese ['A', 42, 'C', 'D']
```

## Dictionaries:
Dictionary is mutable collection of many values. But unlike list it's index(actally called key) can be any value instead of only int. The indexes are called key and
key with it's associated value is called key-value pair together. Dictionaey is written inside '{}'. If two list has same value in same order then they are equal, but two dictionaries with same key-value pair but with different order can be equal.
```bash
>>> spam = ['cats', 'dogs', 'moose'] 
>>> bacon = ['dogs', 'moose', 'cats'] 
>>> spam == bacon 
False 
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'} 
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'} 
>>> eggs == ham 
True
```
Because dictionaries are not ordered, they cant't be sliced like list. Trying to access a key that does not exist in a dictionary will result in a **KeyError** error message, much like a list's "out-of-range" **IndexError** error message. 
```bash
>>> spam = {'name': 'Zophie', 'age': 7} 
>>> spam['color'] 
Traceback (most recent call last):
    File "<pyshell#1>", line 1, in <module>
        spam['color'] 
KeyError: 'color'
```
Dictionaries from python 3.7 and later on remember the insertion-order of their key-value pairs if we create a sequence value from them.
```bash
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'} 
>>> list(eggs) 
['name', 'species', 'age'] 
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'} 
>>> list(ham) 
['species', 'age', 'name']
```
But as fundamentally dictionaries are unordered we just can't access items in them using integer indexes like eggs[0] or ham[2].

### keys(), values() and items() method:
This three methods give sequences of keys, values and key-value pairs(this pair is packed in tuple of each key-value) respectively. This sequences are not list, they 
can't be modified. But we can use for loop in them, in and not in operator in these returned sequences.  We use multiple assignment trick in a for loop to assign the key and value to separate variables.
```bash
>>> spam = {'color': 'red', 'age': 42} 
>>> for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v)) 

Key: age Value: 42 
Key: color Value: red
```

### get() method:
When we want to access value of a key from a dictionary, that key may not be present there and in that situation ```KeyError``` will be thrown. **get(key, default_value) solved it. If the key doesn't exist then default_value will be returned. 
```bash
>>> picnicItems = {'apples': 5, 'cups': 2} 
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.' 
'I am bringing 2 cups.' 
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' 
'I am bringing 0 eggs.'
```

### setdefault(key, value_to_set):
if a key not present in a dictionary then the key and value_to_set will be added in that dictionary as key-value pair. If key existed then it's value would be returned otherwise the value_to_set would be returned.
```bash
>>> spam = {'name': 'Pooka', 'age': 5} 
>>> spam.setdefault('color', 'black') 
'black' 
>>> spam 
{'color': 'black', 'age': 5, 'name': 'Pooka'} 
>>> spam.setdefault('color', 'white') 
'black' 
>>> spam 
{'color': 'black', 'age': 5, 'name': 'Pooka'}
```

### pprint() and pformat() from pprint module:
When we need a well organized view of a dictionary in our stdout, we use ```pprint.print(dictionary)```. If we need organized string representation of a dictionary 
instead of displaying in stdout we will use ```pprint.pformat(dictionary)``` 

## Strings:
indexing, slicing, in and not in works in string as list.

### upper(), lower(), isupper(), islower() methods:
upper() and lower() string methods return a new string where where all the letters in the original string have been converted to uppercase or lowercase, respectively. 
Nonletter charaters in the string remain unchanged. This methods don't mutate original string inseatd they return new string.
```bash
>>> spam = 'Hello, world!' 
>>> spam = spam.upper() 
>>> spam 
'HELLO, WORLD!' 
>>> spam = spam.lower() 
>>> spam 
'hello, world!' 
```
islower() and isupper() they returns boolean value. ```islower()``` returns True if the string contain at least one letter and and all the letters are lowercase. ```isupper()``` returns True if the string contains at least one letter and all the letters are uppercase.

### isalpha():
Returns True if the string only contains letters and isn't blank.
### isalnum():
Returns True if string only contains letters and number and isn't blank.
### isdecimal():
Returns True if string only consists of numeric characters and is not blank.
### isspace():
Returns True if string consists only of space, tabs and newline and is not blank.
### istitle():
Returns True if string consists only of words that begin with an uppercase letter followed by only lowercase letters.

all above isX() are methods.

### startswith() and endswith() methods:
These two methods will return True if the string value they are called on begins or ends with the string passed to method. Otherwise, they return False.

### join() and split() methods:
the join() method is useful when we have a list of strings that need to be joined together. This method called on a string, get passed a list of strings and return a 
string. The returned string is the concatenation of each string in the passed-in-list by the string the method called on.
```bash
>>> ', '.join(['cats', 'rats', 'bats']) 
'cats, rats, bats' 
>>> ' '.join(['My', 'name', 'is', 'Simon']) 
'My name is Simon' 
>>> 'ABC'.join(['My', 'name', 'is', 'Simon']) 
'MyABCnameABCisABCSimon'
```

split() method called on a string and return a list of string. The string on which this method is called splitted into strings by a delimeter string, passed to the method. 
If no delimeter string is passed to the split method then whitespace character will be used as default.
```bash
>>> 'MyABCnameABCisABCSimon'.split('ABC') 
['My', 'name', 'is', 'Simon'] 
>>> 'My name is Simon'.split('m') 
['My na', 'e is Si', 'on']
```

### partition() method:
This method split a string,on which it is called into three string like before the separator(the string passed to the partition method), separator and after the separator.
The method return the 3 splitted string packed into a tuple, and we can use multiple variable assignement trick to extract each string from the returned tuple in three different variable. 
```bash
>>> 'Hello, world!'.partition('w') 
('Hello, ', 'w', 'orld!') 
>>> 'Hello, world!'.partition('world') 
('Hello, ', 'world', '!')
```
If the separator string appears multiple times in the calling string, it will be separated in the first occurance of the separtor.
```bash
>>> 'Hello, world!'.partition('o') 
('Hell', 'o', ', world!')
```
If separator passed does not appear in the calling string, then in the returned tuple whole string will be in the first string's place and other two following string will be empty.
```bash
>>> 'Hello, world!'.partition('XYZ') 
('Hello, world!', '', '')
```

## Justifying text with rjust(), ljust() and center() method:
This three method returne a padded version of the string they are called on. They takes two arguments first is the value which will be length of the new string and second which
is optional(default values is space)  will be a string that will be inserted to match the new string's length. ```rjust()``` insert filling string before the calling string to push the calling string to the right of new string. ```ljust()``` will insert the filling string after the calling string to push the calling string to the left of the new string. 
```center()``` will insert filling string before and after of the calling string to put the calling string in the center of the new string. In the situation center() can not insert equal filling string before and after the calling string to match the mentioned length of the new string in the 1st argument, left part of filling string before calling string makes compromises.
```bash
>>> 'Hello'.rjust(10) 
'     Hello'

>>> 'Hello'.ljust(10) 
'Hello     '

>>> 'Hello'.center(10, '=')
'==Hello==='
```

## strip(), lstrip(), rstrip():
This method called on a string and takes and optional(default value whitespace charset) argument and returned a new string where all whitespace or mentioned charset will be 
missing. ```strip()``` trancate from both left and right, ```lstrip()``` trancate from left side, ```rstrip()``` trancate from right side. The charset order is not important here, to understand look at example.
```bash
>>> spam = ' Hello, World ' 
>>> spam.strip() 
'Hello, World'

>>> spam.lstrip() 
'Hello, World ' 

>>> spam.rstrip() 
' Hello, World'

""" Passing strip() the argument 'ampS' will tell it to strip occurrences of a, m, p, and capital S from the ends of the string stored in spam. The order of the characters in 
the string passed to strip() does not matter: strip('ampS') will do the same thing as strip('mapS') or strip('Spam')
"""
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam' 
>>> spam.strip('ampS') 
'BaconSpamEggs'
```

### ord() and chr() function:
we use ```ord()``` function to get the unicode point of passed one-char string and ```chr()``` to get a char string of an passed unicode point.
```bash
>>> ord('B') 
66 
>>> ord('A') < ord('B') 
True 
>>> chr(ord('A')) 
'A' 
>>> chr(ord('A') + 1) 
'B'
```


### pyperclip module:
This module's copy() and paste() functions that can send text to clipboard and read from clipboard respectively.
```bash
>>> import pyperclip 
>>> pyperclip.copy('Hello, world!') 
>>> pyperclip.paste() 
'Hello, world!'
```
