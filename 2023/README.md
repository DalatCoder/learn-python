# The Complete Python Bootcamp From Zero to Hero in Python

[Udemy](https://udemy.com/course/complete-python-bootcamp)

[Notebooks](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

## Introduction

### Why Python?

Brief History of Python

- Created in 1990 by Guido van Rossum
- Python 3 released in 2008
- Specifically designed as an easy to
  use language
- High focus on readability of code

Why choose Python?

- Designed for clear, logical code that is
  easy to read and learn
- Lots of existing libraries and frameworks
  written in Python allowing users to
  apply Python to a wide variety of tasks
- Focuses on optimizing developer time,
  rather than a computer's processing time
- [Docs](docs.python.org/3)

What can you do with Python?

- This course first focuses on "base" Python,
  which consists of the core components of
  the language and writing scripts and small
  programs.
- Later we begin to learn about outside
  libraries and frameworks that greatly expand
  Python's capabilities
- Automate simple tasks
  - Searching for files and editing them
  - Scraping information from a website
  - Reading and editing excel files
  - Work with PDFs
  - Automate emails and text messages
  - Fill out forms

Data science and machine learning

- Analyze large data files
- Create visualizations
- Perform machine learning tasks
- Create and run predictive algorithms

Create websites

- Use web frameworks such as Django and Flask
  to handle the backend of a website and user
  data
- Create interactive dashboards for users

## Python Setup

### Installing Python

- There are many ways to run Python!
- Later on we'll explore the difference
  between running a Python `.py` script
  or running Python code in a notebook
  environment

Install with Anaconda

- To install Python we will use the free
  Individual Anaconda distribution
- This distribution includes Python as well
  as many other useful libraries, including
  Jupyter Notebook environment.
- Anaconda can also easily be installed on
  to any major OS, Windows, MacOS or Linux

### Running Python code

There are several ways to run Python code.

First, let's discuss the various options
for development environments

- Text editors
- Full IDEs
- Notebook Environments

Text editors:

- General editors for any text file
- Work with a variety of file types
- Can be customized with plugins and add-ons
- Keep in mind, most are not designed
  with only Python in mind

Full IDEs

- Development Environments designed speccifically for Python
- Larger programs
- Only community editions are free
- Designed specifically for Python, lots
  of extra functionality

Notebook Environments

- Great for learning
- See input and output next to each other
- Support in-line markdown notes,
  visualizations, videos, and more
- Special file formats that are not `.py`

## Python Basics

### Data Types

Some types:

- `int`: Integers, whole numbers
- `float`: Floating point, numbers with a decimal point
- `str`: Strings, ordered sequence of characters
- `list`: Lists, ordered sequence of objects
- `dict`: Dictionaries, unordered key:values pairs
- `tup`: Tuples, ordered immutable sequence of objects
- `set`: Sets, unordered collection of unique objects
- `bool`: Booleans,logical value

### Numbers

There are two main number types:

- Integers
- Floating point

Operators:

- `+`
- `-`
- `*`
- `/`
- `%`: mod
- `**`: power

### Variable assignments

Rules for variable names

- Names can not start with a number
- There can be no spaces in the name, use `_` instead
- Can't use any of these symbols: `'",<>/?|\()!@#$%^&*~-+`
- It's considered best practice (`PEP8`) that
  names are lowercase
- Avoid using words that have special
  meaning in Python like `list` and `str`

Other notes

- Python uses `Dynamic Typing`
- This means you can reassign variables to
  different data types
- This makes Python very flexible in assigning
  data types, this is different that other
  languages that are `Statically Typed`

Pros of Dynamic typing:

- Very easy to work with
- Faster development time

Cons of Dynamic typing:

- Many result in bugs for unexpected data types
- You need to be aware of `type()`

### Introduction to Strings

Strings are sequences of characters, using
the syntax of either single quotes or
double quotes:

- `'hello'`
- `"Hello"`
- `"I don't do that"`

Because strings are `ordered sequences`, it
means we can using `indexing` and `slicing`
to grab sub-sections of the string.

Indexing notation uses `[]` notation after the
string (or variable assigned the string)

Indexing allows you to grab a single
character from the string

- `h`, `e`, `l`, `l`, `o`
- `0`, `1`, `2`, `3`, `4`, `5`
- `0`, `-4`, `-3`, `-2`, `-1`

Slicing allows you to grab a subsection of
multiple characters, a `slice` of the string.

This has the following syntax: `[start:stop:step]`

- `start`: is a numberical index for the slice start
- `stop`: is the index you will go up to (but not include)
- `step` is the size of the `jump` you take

```py
my_str = 'Hello World'

print(my_str[0]) # 'H'
print(my_str[1]) # 'e'
print(my_str[len(my_str) - 1]) # 'd'
print(my_str[len(my_str) - 2]) # 'l'
print(my_str[-1]) # 'd'
print(my_str[-2]) # 'l'

print(my_str[2:]) # 'llo World'
print(my_str[0:3]) # 'Hel'
print(my_str[2:3]) # 'l'
print(my_str[::]) # 'Hello World'
print(my_str[::2]) # 'Hlo ol'
print(my_str[::-1]) # 'dlroW olleH'
```

### String properties and methods

Immutability: you cannot mutate or cannot change

```py
name = 'Hieu'
name[1] = 'a' # error

b = name[:1] + 'a' + name[2:]

letter = 'z'
letter * 10 # zzzzzzzzzzz

letter + 3 # error
letter + str(3) # z3
```

Operators

- `+`: concatenation
- `*`: multiplication of letters

String methods

- `str.upper()`
- `str.lower()`
- `str.split()`

### String formatting for printing

There are multiple ways to format strings
for printing variables in them. This is
known as `string interpolation`

Let's explore two methods for this

- `.format()` method
- `f-strings` (formatted string literals)

Formatting with the `.format()` method

```py
a = 'String here {} then also {}'.format('1', '2')

a = 'String here {0} then also {0}'.format('1', '2')

a = 'The {q} {b} {f}'.format(f='fox',b='brown',q='quick')
```

Float formatting follows `{value:width.precision f}`

```py
result = 100 / 777

print('result {r:1.3f}'.format(r=result)) # 0.129
```

Using formatted string literals (>3.6)

```py
name = 'Hieu'
print('Hello his name is {}'.format(name))
print(f'Hello his name is {name}')
```

## Lists

- Lists are `ordered sequences` that
  can hold a variety of object types
- They use `[]` brackets and commas to
  seperate objects in the list
- Lists support `indexing` and `slicing`.
- Lists can be nseted and aslo have a variety
  of useful methods that can be called off
  of them.
- You can actually mutate or change the
  elements that are already in a list

```py
my_list = [1,2,3]
my_list = [1,'a',true]

my_list[0] # 1
my_list[1:2] # 2
my_list[-1] # 3

a = [1,2]
b = [3,4]
c = a + b # [1,2,3,4]
```

Methods

```py
a = [1,2]

a.append(3) # [1,2,3]
a.pop() # 3
a.pop(0) # 1
```

### Dictionaries

- Dictionaries are `unordered` mappings
  for storing objects. Previously we saw
  how lists store objects in an ordered
  sequence, dictionaries use a key-value
  pairing instead.
- This key-value pair allows users to quickly
  grab objects without needing to know an
  index location
- Dictionaries use curly braces and colons
  to signify the keys and their associated
  values: `{'key1': 'value'}`

When to choose a `list` and when to choose a
`dictionary`?

- `dictionaries`: objects retrieved by `key` name. Unordered and cannot be sorted
- `lists`: objects retrived by location. Ordered sequence can be indexed or sliced.

```py
my_dict = {
    'name': 'Hieu',
    'age': 23
}

print(my_dict['name'])
print(my_dict['age'])

prices_lookup = {
    'apple': 2.99,
    'oranges': 1.99,
    'milk': 5.80
}
print(prices_lookup['apple'])

prices_lookup['flower'] = 9.99

prices_lookup.keys()
prices_lookup.values()
prices_lookup.items()
```

### Tuples

- Tuples are very similar to lists. However they have one key difference - `immutability`
- Once an element is inside a tuple, it can not be reassigned
- Tuples use parenthesis: `(1,2,3)`

Using tuples when

- Passing around objects in your program and
  you need to make sure that they don't accidentally get changed

- Provides a very convenient source of what's known as `data integrity`

### Sets

- Sets are unordered collections of `unique`
  elements
- Meaning there can only be one representative
  of the same object

```py
my_set = set()

my_set.add(1) # {1}
my_set.add(2) # {1,2}
my_set.add(2) # {1,2}
```

Using when:

- Casting a list to a set that we only get
  the unique values

```py
my_list = [1,2,3,1,1,1]
unique = set(my_list) # {1,2,3}
```
