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

### Booleans

- Booleans are operators that allow you
  to convey `True` or `False` statements

- There are very importatn later on when we
  deal with control flow and logic

```py
true = True
false = False

type(true) # bool
type(false) # bool
```

### I/O with basic files in Python

Using jupyter notebook to quickly write a file

```ipynb
%%writefile myfile.txt
Hello this is a text file
this is the second line
```

Open file

```py
my_file = open('myfile.txt')

my_file.read() # receive all content
my_file.read() # ''
```

There is a `cursor` at the beginning of the
file. when you read it `.read()`, the `cursor`
goes all the way to the end of the file and
you need to `reset` the `cursor` or `seek` it
back to `0` in order to `.read()` it again.

```py
my_file = open('myfile.txt')

my_file.read() # receive all content

my_file.seek(0)
my_file.read() # receive all content
```

Sometimes, the `.read()` method is not really
useful because you'd actually want to have
a list where each single element in the list
is one line in a string form of the actual
text file.

```py
my_file = open('myfile.txt')

my_file.read() # receive all content

my_file.seek(0)
my_file.readlines() # list of string lines
```

Close file after working with it

```py
my_file = open('myfile.txt')

my_file.read() # receive all content
my_file.close()
```

Using `with` to automatically close file

```py
with open('my_file.txt') as my_file:
    contents = my_file.readlines()
```

Write files

```py
with open('my_file.txt', mode='w') as my_file: 
    my_file.write('Hello World')

with open('my_file.txt', mode='a') as my_file: 
    my_file.write('Hello World')
```

File permissions

- `r`: only `read`
- `w`: only `write`, (will overwrite files or create new)
- `a`: only `append` (add on to files)
- `r+`: reading and writing
- `w+`: writing and reading (overwrites existing files or creates a new file)

### Comparison Operators

Operators

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

Logical operators

- `and`
- `or`
- `not`

## Python Statements

### If-else

- Let's begin to learn about control flow
- We often only want certain code to execute
  when a particular condition has been met
- To control this flow logic, we use some
  keywords:
  - `if`
  - `elif`
  - `else`
- Control flow syntax makes use of colons
  and indentation (whitespace)
- This indentation system is crucial to
  Python and what sets it apart from other
  programming languages

```py
loc = 'Bank'

if loc == 'Auto Shop':
    pass
elif loc == 'Bank':
    pass
else 
    pass
```

### For loop

- Many objects in `Python` are `iterable`,
  meaning we can iterate over every element in
  the object.
- Such as every element in a `list` or every
  character in a `string`
- We can use for loops to execute a block of
 code for every iteration
- The term `iterable` means you can `iterate`
  over the object

```py
my_list = [1,2,3,4,5]

for n in my_list:
    print(n)

for letter in "Hieu":
    print(letter)

for n in (1,2,3):
    print(n)

my_list = [('a',1), ('b',2)]

# tuple unpacking
for a,b in my_list:
    print(a,b)

d = {
    'a': 1,
    'b': 2
}

for k,v in d.items():
    print(k,v)
```

### While loop

While loops will continue to execute a block
of code while some condition remains `True`

For example, while my pool is not full, keep
filling my poll with water. Or while my dogs
are still hungry, keep feeding my dogs.

```py
while True:
    pass
else:
    pass
```

We can use some statements inside the loop

- `break`: breaks out of the current closest
  enclosing loop
- `continue`: goes to the top of the closest
  enclosing loop
- `pass` does nothing at all

### Useful operators

- `range` is a generator. It is just a special type of function that will generate informatioin instead of saving it all to memory. This a more efficient way of generating these numbers instead of having a giant sorted memory.

```py
for num in range(2):
    print(num) # 0 1 2 

l = list(range(1,5)) # [1,2,3,4]
```

- `enumerate`, get `index` and `value`

```py
index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))

    index_count += 1

for index,letter in 'abcde':
    print(index,letter)
```

- `zip`, kind of almost like an opposite of `enumerate`. What is does is it zips together
  to lists.

```py
mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for num,cha in zip(mylist1, mylist2):
    print(num,cha)

l = list(zip(mylist1, mylist2))
```

- `in`: check if value exists in a list

```py
'x' in [1,2,3] # False
'1' in [1,2,3] # True
'a' in 'hello world' # False
'k' in { 'k': 1 } # True
```

### List Comprehensions

List comprehensions are a unique way of
quickly creating a list with `Python`

If you find yourself using a for loop along
with `.append()` to create a `list`. List
comprehensions are a good alternative!

```py
name = 'Hieu'
list_name = []

for letter in name:
    list_name.append(letter)
```

Using list comprehensions to flatten the for loop

```py
name = 'Hieu'
list_name = []

# for letter in name 
# put letter in front of the for statement
list_name = [letter for letter in name]
my_list = [x for x in 'hello world']
my_list = [x for x in range(0,11)]
my_list = [x**2 for x in range(0,11)]
my_list = [x for x in range(0,11) if x%2==0]
```

## Methods and Functions

### Methods

Built-in objects in Python have a variety
of methods you can use!

Let's explore in a bit more detail how to find
methods and how to get information about them.

```py
l = [1,2,3]

l.append(4)
l.pop()
l.pop(0)

help(l.insert)
```

[Python Docs](https://docs.python.org/3/)

### Functions

Crreating clean repeatable code is a key
part of becoming an effective programmer

Functions allow us to create blocks of
code that can be easily executed many
times, without needing to constantly
rewrite the entire block of code

Functions will be a huge leap forward
in your capabilities as a Python programmer.

This means that the problems you are
able to solve can also be a lot harder!

#### `def` keyword

Creating a function requires a very
specific syntax, including the `def` keyword,
correct indentation, and proper structure.

```py
def name_of_function():
    '''
    Docstring explains function
    '''
    pass

name_of_function()
```

Args

```py
def greet(name):
    print('Hello ' + name)

greet('Hieu')
```

Typically we use the `return` keyword to
send back the result of the function, instead
of just printing it out.

`return` allows us to assign the output of
the function to a new variable.

```py
def add(n1, n2):
    return n1 + n2
```

#### Basic function

Provide default args

```py
def greet(name = 'Stranger'):
    print('Hello ' + name)

greet('Hieu')
greet()
```

#### Functions with logic

```py
def even_check(number):
    return number % 2 == 0

def check_even_list(num_list):
    even_numbers = []
    for n in num_list:
        if n % 2 == 0:
            even_numbers.append(n)

    return even_numbers
```

#### Tuple unpacking with Python functions

Re all that we've previously seen, we can loop
through a list of tuples and unpack the values within them.

```py
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item)

# unpacking
for ticker,price in stock_prices:
    print(ticker)
```

Work with function

```py
work_hourse = [
    ('Abby', 100),
    ('Billy', 400),
    ('Cassie', 800)
]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return (employee_of_month, current_max)

employee,hour = employee_check(work_hours)
```

#### Interaction between functions

```py
from random import shuffle

l = [1,2,3,4,5]
shuffle(l)

print(l)

def player_guess():
    guess = ''
    
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1 or 2')

    return int(guess)
```

### `*args` and `**kwargs` in Python

- `args`: Arguments
- `kwargs`: Keyword arguments

```py
def add(*args):
    print(type(args)) # tuple

    for item in args:
        pass

    return sum(args)

add(1,2)
add(1,2,3)
add(1,2,3,4)
```

```py
def myfunc(**kwargs):
    print(type(kwargs)) # dictionary

    if 'fruit' in kwargs:
        print('My fruit of choice is ' + kwargs['fruit'])
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple', veggie='lettuce')
```

The convention is to use `args` and `kwargs`.
However, we can choose whatever names we like

```py
def add(*numbers):
    pass

def func(**dict):
    pass
```

Used in combination

```py
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(10,20,30,fruit='orange',food='egg')
```

This allows you to take in an arbitrary number
of arguments that you don't need to define
beforehand. And this is going to be especially
useful when you begin to use outside library.

### Lambda expressions: Map and Filter

```py
def square(n):
    return n**2

numbers = [1,2,3,4,5]
square_numbers = []

for n in numbers:
    square_numbers.append(square(n))
```

Or using `map`

```py
def square(n):
    return n**2

numbers = [1,2,3,4,5]
square_numbers = list(map(square, numbers))
```

`filter` function

```python
def check_even(num):
    return num % 2 == 0;

numbers = [1,2,3,4,5]
even_numbers = list(filter(check_even, number))
```

Lambda expressions (anonymous function)

```py
def square(n):
    result = num**2
    return result

square(3)

square_lambda = lambda num: num**2
square_lambda(3)
```

Using `lambda` with `map` and `filter`

```py
numbers = [1,2,3,4,5]
evens = list(filter(lambda n:n%2==0, numbers))
squares = list(map(lambda n:n**2, numbers))
```

### Nested statements and Scope

It's important to understand how Python deals
with the variable names you assigned. When
you create a variable name in Python, that
name is stored in what's called the `namespace`, and variable names also have a
`scope`. And the `scope` determines the
visibility of that variable name to
other parts of your code.

```py
x = 25

def printer():
    x = 50
    return x

print(x) # 25
print(printer()) # 50
```

scope allows Python to understand and have
a set of rules to decide which variables
you're referencing in your code.

`LEGB` rule, this is the order that Python is going to look for variables.

- `L`: Local - Names assigned in any way within a function (def or lambda), and not declared global in that function

- `E` Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer. Nested functions

- `G`: Global (module) - Names assigned at the top-level of a module file, or declared global in a `def` within the file

- `B`: Built-in (Python) - Names preassigned in the built-in names module

```py
# Global
name = 'This is a global string'

def greet():
    # Enclosing
    name = 'Sammy'

    def hello():
        # Local
        name = 'Im a local'

        print('Hello ' + name)
    hello()

greet() # Hello Sammy
```

Reassign global variable with `global` keyword

```py
x = 50

def func():
    global x
    x = 200
```

Avoid using `global` keyword

```py
x = 50

def func(x):
    return 200

x = func(x)
```

## Milestone Project - 1

### Introduction to Warm Up Project Exercises

Most programs that are interactive work
on this very simple idea

- Display something visual to the user
- Let the user update through an interaction
- Update variables in the program
- Display updated visual

### Displaying Information

```py
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ', ' ', ' ']
row2 = [' ', 'X', ' ']
row3 = [' ', ' ', ' ']

display(row1,row2,row3)
```

### Accepting user input

```py
input('Please enter a value')
```

### Validating user input

```py
def user_choice():
    choice = ''
    acceptable_range = range(0,10)
    within_range = False

    while not choice.isdigit() or not within_range:
        choice = input('Please enter a number (0-10): ')

        if not choice.isdigit():
            print('Sorry that is not a digit!')

        if int(choice) in acceptable_range:
            within_range = True

    return int(choice)
```

### Overview

Tic Tac Toe game for 2 human players.

Let's describe what the game will be like

- 2 players should be able to play the game
- The board should be printed out everytime
  a plyaer makes a move
- You should be able to accept input of the
  player position and then place a symbol on
  the board

We will use the `numpad` to match numbers
to the grid on a tic tac toe board.

```py
board = [
    7, 8, 9,
    4, 5, 6, 
    1, 2, 3,
]
```

### Solutions

```py
from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker = ''

    while marker not in ['X', 'O']:
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    
    return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (board[7] == mark and board[8] == mark and board[9] == mark) or (pass)

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False

    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position'))

    return position

def replay():
    choice = input('Play again? Enter Yes or No')
    return choice == 'Yes'

def main():
    print('Welcome to Tic Tac Toe')

    while True:
        ## Set everyting up
        the_board = [' '] * 10
        player1_marker,player2_marker = player_input()

        turn = choose_first()
        print(turn + ' will go first')

        play_game = input('Ready to play? y or n? ')
        if play_game == 'y':
            game_on = True
        else:
            game_on = False

        ## game play
        while game_on:
            if turn == 'Player 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player1_marker,position)
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print('PLAYER 1 HAS WON!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('TIE GAME!')
                        game_on = False
                    else:
                        turn = 'Player 2'
            else:
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player2_marker,position)
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print('PLAYER 2 HAS WON!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('TIE GAME!')
                        game_on = False
                    else:
                        turn = 'Player 1'

        if not replay():
            break

main()
```

## Object Oriented Programming

### Introduction to OOP

OOP allows programmers to create their own
objects that have methods and attributes .

Recall that after defining a string, list, dictionary, or other
objects, you were able to call methods off of them with
the `.method_name()` syntax.

These methods act as funcions that use
informatioin about the object, as well as the
object itself to return results, or change the
current object

For example this includes appending to a list,
or counting the occurences of an element in
a tuple.

OOP allows users to create their own object.

The general format is often confusing when first encountered,
and its usefulness may not be completely clear at first

In general, OOP allows us to create code that is repeatable and
organized.

For much larger scripts of Python code,
functions by themselves aren't enough for
organization and repeatability.

Commonly repeated tasks and objects can be defined
with OOP to create code that is more usable.

```py
class NameOfClass():
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        pint(self.param1)
```

### Class Attributes

Simple class

```py
class Sample():
    pass

my_sample = Sample()
type(my_sample) # __main__.Sample
```

Constructor (`__init()__`)

```py
class Dog():
    def __init__(self, breed):

        # attributes
        self.breed = breed

lab = Dog(breed='Lab')
huskie = Dog(breed='Huskie')

print(lab.breed)
print(lab.huskie)
```

### Class Methods

Methods are essentially functions defined inside the body of
the class, and they're used to perform operations that sometimes
ultilize the actual attributes of the object we created.

```py
class Dog():
    species = 'mammal'

    def __init__(self,breed,name):
        # attributes
        self.breed = breed
        self.name = name

    # operations/actions --> methods
    def bark(self):
        print("WOOF! My name is {}".format(self.name))

lab = Dog(breed='Lab',name='Sam')

print(lab.breed)
print(lab.name)
print(lab.species)
```

```py
class Circle():

    # Class object attribute
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2

c = Circle(2)
c.get_circumference()
```

### Inheritance and Polymorphism

Inhertitance is basically a way to form new classes using
classes that have already defined. The benefits of inheritance
are the ability to reuse code that you've already worked on and
reduce the complexity of a program.

```py
# base class
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

a = Animal()
a.who_am_i()
a.eat()
```

The `Dog` class inherits from the `Animal` class

```py
# Derived class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    # override base method
    def who_am_i(self):
        print('I am a dog')

    def bark(self):
        print('WOOF!')

d = Dog()
d.who_am_i()
d.eat()
```

In Python, polymorphism refers to the way in which
different object classes can share the same method name.
and then those methods can be called from the same
place, even though a variety of different objects might be passed
in.

```py
class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'

niko = Dog('niko')
felix = Cat('felix')

niko.speak()
felix.speak()

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

# don't care what pet actually is
# only care about the speak method on each pet
# commonly used
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
```

A more common practice is to use `abstract clsases` and
`inheritance`.

```py
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
```

```py
class Dog(Animal):
    def speak(self):
        return self.name + ' says woof!'

class Cat(Animal):
    def speak(self):
        return self.name + ' says meow!'

fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())
```

### Special (Magic/Dunder) methods

Special methods allow us to use some built-in operations
in Python, such as the `length` function or the `print`
function with our own user created objects.

```py
l = [1,2,3]
len(l)
print(l)

class Sample():
    pass

s = Sample()
len(s)
print(s)
```

Special methods, some people also call them magic methods or
dunder methods because they use `__`

```py
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

b = Book('Python rocks', 'Jose', 200)

print(b)
string_representation = str(b)
print(len(b))

# delete variable
del b
```

## Modules and Packages

### Pip Install and Pypi

PyPI is a repository for open-source third-party Python packages

It's similar to RubyGems in the Ruby world, PHP's Packagist,
CPAN for Perl and NPM for Node.js

So far, we've really only used libraries that come internally
with Python (standard libraries). There are many other libraries available that
people have open-sourced and shared on PyPI.

We can use `pip install` at the command line to install these
packages.

Pip is a simple way to download packages at your command line
directly from the PyPI repository.

```sh
pip install requests
pip install colorama
```

### Modules & Packages

Now that we understand how to install external packages,
let's explore how to create our own modules and packages.

`Modules` are just `.py` scripts that you call in another `.py`
script.

`Packages` are a collection of modules.

#### Create a module

Module is just a `.py` script being called in from another file.
The idea is that if you have a really large script, you're not
going to put everything in one giant `.py` file. Instead, it'll be
nice to split up between multiple `.py` files, which means you
split it up between different `modules`.

And then later we'll see how we can aggregate a bunch of modules
to create a package.

```py
# module.py

def my_func():
    print('Hey I am in module.py')
```

```py
# main.py

from module import my_func

my_func()
```

#### Create a package

- Create new folder called `MyMainPackage`
- Create new folder called `MyMainPackage/SubPackage`

Now, since these are just directories or folders, we need to
let Python be able to understand that we want to treat these
directories not just as a normal directory but as an actual package.

- Create new file called `MyMainPackage/__init__.py`
- Create new file called `MyMainPackage/SubPackage/__init__.py`

Now, you don't actually need to write anything in this file.
It just needs to be there so that when Python goes searching
through these packages, it understands that it's not just a normal
directory. It's an actual `package`.

- Create new file `MyMainPackage/main_script.py`
- Create new file `MyMainPackage/SubPackage/sub_script.py`

```py
# sub_script.py

def sub_report():
    print('Hey I am a function inside sub_script.py')
```

```py
# main_script.py

def main_report():
    print('Hey I am in main_script.py')
```

Import from `package`

```py
# main.py

from MyMainPackage import main_package
from MyMainPackage.SubPackage import sub_package

main_package.main_report()
sub_package.sub_report()
```

Directories:

- `main.py`
- `module.py`
- `MyMainPackage`
  - `__init__.py`
  - `main_script.py`
  - `SubPackage`
    - `__init__.py`
    - `sub_script.py`

### `__name__` and `__main__`

An often confusing part of Python is a
mysterious line of code: `if __name__ == "__main__":`

Sometimes when you are importing from a module,
you would like to know wheter a module function is being
used as an import, or if you are using the original `.py` file
of that module.

Create a file called `one.py`

When we run `python one.py`, all the code defined at indentation
level `0` will be executed.
And there is no `main` function for `entry point`

There is `__name__` variable that is built-in to Python. So what
happens is this variable `__name__` gets assigned a string depending
on how you're running the actual script and if you run the script
directly `python one.py`. It's going to assign this builtin variable
called `__name__` to be equal to `__main__`. So Python does this
in the background.

So if `__name__` equal to `__main__`, you know that this particular
`.py` file is being run directly.

```py
# one.py

def func():
    print('FUNC() IN ONE.PY')

print('TOP LEVEL IN ONE.PY')

if __name__ == "__main__":
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')
```

In `two.py`

```py
# two.py

import one

print('TOP LEVEL IN TWO.PY')

one.func()

if __name__ == '__main__':
    print('TWO.PY is being run directly!')
else:
    prinit('TWO.PY has been imported!')
```

Open commandline and run:

- `python one.py`
- `python two.py`

> So that builtin variable actualy allows you to see wheter something
> is being imported or run directly.

Conventions

```py
def func():
    pass

def func1():
    pass

if __name__ == "__main__":
    # RUN THE SCRIPT!
    func()
    func1()
```

## Errors and Exceptions Handling

### Intro

- Errors are bound to happen in your code!
- Especailly when someone else ends up using it in an unexpected
  way
- We can use error handling to attempt to plan for possible errors

Error handling

- `try`: this is the block of code to be attempted (may lead to an error)
- `except`: block of code will execute in case there is an error in `try` block
- `finally`: a final block of code to be executed, regardless of an error

```py
try:
    f = open('t.txt', 'r')
    f.write('write a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS error')
except:
    print('All other exceptions')
finally:
    print('I always run')
    f.close()
```

```py
def ask_for_input():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops! That is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('End of try/except/finally')
            print('I will always run at the end!')
```

### Pylint overview

As you begin to expand to larger multi-file projects. It becomes
important to have tests in place.

This way as you make changes or update your code, you can run your
test files to make sure previous code still runs as expected.

There are several testing tools, we will focus on two:

- `pylint`: this is a library that looks at your code and reports
  back possible issues
- `unittest`: this built-in library will allow to test your own
  programs and check you are getting desired outputs

We'll begin by showing you how to use `pylint` to check your code
for possible errors and styling.

Python as a set of style convention rules known as `PEP 8`

Install `pylint` library: `pip install pylint`

Create new script file

```py
# test.py
a = 1
b = 2

print(a)
print(c)
```

Run `pylint test.py`

### Running tests with the UnitTest Library

UnitTest allows you to write your own test program.
And the goal is to send a specific set of data to your program,
analyze the returned results, and then see if it actually gives
you the expected result.

Create 2 scripts:

- `cap.py`
- `test_cap.py`

In `cap.py`

```py
# cap.py

def cap_text(text):
    return text.title()
```

In `test_cap.py`

```py
# test_cap.py

import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        expected = 'Python'

        self.assertEqual(result, expected)

    def test_multiple_words(self):
        text = 'hello world'
        result = cap.cap_text(text)
        expected = 'Hello World'

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
```

Run test

```sh
python test_cap.py
```

## Decorators

Decorators allow you to `decorate` a function.

You have a function

```py
def func():
    # Something
    pass
```

Now, you want to add some new capabilities to the function by editting the old function

```py
def func():
    # Something
    # Another things
    pass
```

You now have two options

- Add that extra code to your old function
- Create a brand new function that contanis the old code,
  and then add new code to that

But what if you then want to remove that extra `functionality`

- You would need to delete it manually, or make sure to have
  the old function
- Is there a better way? Maybe an on/off switch to quickly
  add this functionality?

Decorators

- Python has `decorators` that allow you to tack on
  extra functionality to an already existing function
- They use the `@` operator and are then placed on top
  of the original function

Now you can easily add on extra functionality with a decorator

```py
@some_decorator
def func():
    # Something
    pass
```

This idea is pretty abstract in practice with Python syntax,
so we will go through the steps of manually building out a
decorator ourselves, to show what the `@` operator is doing
behind the scenes.

```py
def func():
    return 1

func()

# assign function to variable
f = func
f()
```

Passing funtion

```py
def hello(name = 'Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\tThis is the greet() function inside hello'

    def welcome():
        return '\tThis is welcome() inside hello'
    
    print(greet())
    print(welcome())

    print('This is the end of the hello() function')

hello()
greet() # welcome is not defined | out of scope
welcome() # welcome is not defined | out of scope
```

Function return function

```py
def hello(name = 'Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\tThis is the greet() function inside hello'

    def welcome():
        return '\tThis is welcome() inside hello'

    if name == 'Jose':
        return greet
    return welcome

fn = hello()
fn()
```

Passing function as an argument

```py
def hello():
    return 'Hi Jose!'

def other(some_fn):
    print('Other code runs here!')
    print(some_fn())

other(hello)
```

So now we understand that we can return functions and we can
have functions arguments with those two main tools, we're actually
going to now be able to create a `decorator`.

We have the tools we need to quickly create some sort of device
that is an on/off switch when we want to add more functionality
to a `decorator`.

```py
def new_decorator(original_func):

    # extra functionality inside wrap_func
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function')

    return wrap_func
```

The actual original function is the present, and then we're going
to essentially put it inside a box and wrap aroud it, which is
why this is called `decoration`. So you're kind of
decorating this function with some wrapping paper.

```py
def func(): 
    print('I want to be decorated')

new_decorator(func)()

decorated_func = new_decorator(func)
decorated_func()
```

Sugar syntax

```py
# turn on
@new_decorator
def func(): 
    print('I want to be decorated')

# turn off
# @new_decorator
def func(): 
    print('I want to be decorated')

func()
```

When you are going to be using a web framework or someone else's
library and just adding in these new decorators to maybe render
a new website or point to another page.

So they're really commonly used in web frameworks such as
Django or Flask, which is why it's important to understand
behind the scenes what the decorator is actually doing.

## Generators

We've learned how to create functions with `def` and the `return`
statement.

`Generator` functions allow us to write a function
that can send back a value and then later resume to pick up where it
left off.

This type of function is a generator in Python, allowing us to
generate a sequence of values over time. The main different in
syntax will be the use of a `yield` statement.

When a `generator` function is compiled, they become an object
that supports an `iteration protocol`.

that means when they are called in your code they don't actually
return a value and then exit.

Generator functions will automatically suspend and resume
their execution and state around the last point of value
generation.

The advantage is that instead of having to compute an entire
series of values up front, the `generator` computes one values
and waits until the next value is called for.

So you can imagine if you wanted to get all the numbers between
`1` and `1.000.000`, you have two options

- start generating values `1`, `2`, `3`,... and continue to
  feed them that way in the for loop

- or you would create a giant list of numbers [1..1000000] and
  then slowly pick of those numbers from memory

For example, the `range()` function doesn't produce an list
in memory for all the values from start to stop. Instead, it
just keeps track of the last number and the step size, to provide
a flow of numbers.

If a user did need the list, they have to transform the generator
to a list with `list(range(0,10))`

Normal function

```py
def create_cubes(n):
    result = []

    for x in range(n):
        result.append(x**3)

    return result

create_cubes(1000000)
```

What if we just one 1 value at a time in a for loop instead of
that whole list stored in memory.

In fact, we just need the previous value and then whatever
the formula is to get to the next value in order to generate
all the values.

Generator

```py
def create_cubes(n):
    for x in range(n):
        yield x**3

for x in create_cubes(1000000):
    print(x)
```

Get list of `fibonaci` numbers

```py
def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)
```

The key to fully understanding `generators` is the `next` function
and the `iter` function.

```py
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # StopIteration Error

# for loop automatically catches this error and stops calling next
```

The `iter` function basically allows us to automatically iterate
through a normal object that you may not expect.

```py
s = 'hello'

for letter in s:
    print(letter)

next(s) # error

s_iter = iter(s)
next(s_iter) # h
next(s_iter) # e
next(s_iter) # l
next(s_iter) # l
next(s_iter) # o
```

## Advanced Python Modules

### Section intro

Python has several built-in modules that we haven't fully explorered
yet!

Modules covered in this section:

- Collections
- OS Module and Datetime
- Math and Random
- Python debugger
- Timeit
- Regular expressions
- Unzipping and zipping modules

### Collections module

- `Counter`

```py
from collections import Counter

my_list = [1,1,1,2,2,3,3,3,4,5]
Counter(my_list)
Counter('helloworld')

sentence = 'How many times does each word show up in this sentence with a word'
Counter(sentence.lower().split())
```

Some common patterns with `Counter`

```py
my_list = [1,1,1,2,2,3,3,3,4,5]
c = Counter(my_list)
c.most_common()
```

- `defaultdict`
- `namedtuple`

### Opening and Reading files and Folder

`shutil` and `os` modules

We already know how to open an individual file with Python, but
we still don't know how to do a few things:

- What if we have to open very file in a directory?
- What if we want to actually move files aroud on our computer?

Python's `os` moudle and `shutil` (shell utilities) allow us to
easily navigate files and directories on the computer and then
perform actions on them, such as moving them or deleting them.

Get current directory

```py
import os

print(os.getcwd())
print(os.listdir())
```

To move files

```py
import shutil

shutil.move('test.txt', '/root/dest/')
```

### Datetime module

```py
import datetime

my_time = datetime.time()
today = datetime.date.today()
```

Datetime

```py
from datetime import datetime
```

Date

```py
from datetime import date
```

### Math and Random modules

```py
import math

help(math)
```

```py
import random
random.seed(101)
random.randint(0,100)
```

### Python debugger

When trying to figure out what errors there are in your code, you've
probably used `print()` to try to track down the error. Fortunately,
Python comes with a built-in debugger tool that allows you to
interactively explore variables within mid-operation
of your Python code.

```py
import pdb

a = 1
b = 2

pdb.set_trace()

result = a + b
```

To quit, type `q`

### Python Regex

We already know we can search for substrings within a larger
string with the `in` operator

- `"dog" in "my dog is great"` --> `True`
- `"dog" in "my cat is great"` --> `False`

This has severe limitatiions, we need to know the exact string, and
need to perform additional operations to account for capitalization
and punctuation.

What if we only know the pattern structure of the string we're
looking for? Like an email or phone number?

Regular Expressions (regex) allow us to search for general
patterns in text data!

For example, a simple email format can be: `user@email.com`.
We know in this case we're looking for a pattern:
`text` + `@` + `text` + `.com`

So what I can use regex for is to construct a generalized
pattern to search for something like this.

The `re` library allows us to create specialized pattern strings
and then search for matches within text. The primary skill set
for regex is understanding the special syntax for these
pattern strings.

Don't feel like you need to memorize these patterns! Focus on
understanding how to look up the information.

- Phone number: `(555)-555-5555`
- Regex pattern: `r"(\d\d\d)-\d\d\d-\d\d\d\d"`

  - `r""`: python syntax
  - `\d`: pattern for a digit
  - `( ) - -`: exact text

- Or: `r"(\d{3})-\d{3}-\d{4}"`

Using `regex` to find a normal string

```py
text = "The agent's phone number is 408-555-1234. Call soon!"

if 'phone' in text:
    pass

import re

pattern = 'phone'
match = re.search(pattern, text)

match.span() # get first actual index
math.start() # first start index
match.end() # first end index

matches = re.findall(pattern, text)

for match in re.finditer(pattern, text):
    match_text = match.group()
    pass
```

Regular expressions patterns: `Identifiers`

- `\d`: A digit (placeholder for any digits), `file_\d\d` -> `file_25`
- `\w`: Alphanumeric (a letter or a number), `\w-\w\w\w` -> `A-b_1`
- `\s`: White space, `\a\sb\sc` -> `a b c`
- `\D`: A non digit, `\D\D\D` -> `ABC`
- `\W`: Non-alphanumeric, `\W\W\W\W\W` -> `*-+=)`
- `\S`: Non-whitespace, `\S\S\S\S` -> `Yoyo`

```py
text = 'My phone number is 408-555-1234'

phone = re.search('408-555-1234', text)
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
```

Regular expressions patterns: `Quantifiers`

- `+`: Occurs one or more times, `Version \w-\w+` -> `Version A-b1_1`
- `{3}`: Occurs exactly 3 times, `\D{3}` -> `abc`
- `{2,4}`: Occurs 2 to 4 times, `\d{2,4}` -> `123`
- `{3,}`: Occurs 3 or more, `\w{3,}` -> `anycharacters`
- `{*}`: Occurs zero or more times, `A*B*C*` -> `AAACC`
- `?`: Once or none, `plurals?` -> `plural`

```py
text = 'My phone number is 408-555-1234'

phone = re.search('408-555-1234', text)
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
```

Now we want to do two tasks as the same time

- Extract the area code `408`
- Extract the full phone number `408-555-1234`

What we can do is we can use groups for any general tasks
that involes grouping together regex. Using `()` to group.

```py
text = 'My phone number is 408-555-1234'

# compile 3 group
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
results.group()

results.group(1) # area code
results.group(2)
results.group(3)
```

Addtional regex syntax

- or: `re.search(r'cat|dog', 'The cat is here')`
- wildcard: `re.findall(r'.at', 'The cat is here')`
- start with: `^`
- end with: `$`

### Timing your Python code

As you learn more Python, you will
discover multiple solutions for a single task
and you may find yourself trying to figure
out the most efficient approach.

An easy way to do this is to time your code's
performance.

We will focus on 3 ways of doing this:

- Simply tracking time elapsed
- Using the `timeit` module
- Special `%%timeit` magic for Jupyter notebooks

```py
def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))

func_one(10)
func_two(10)
```

Simple solutions

```py
# current time before
start_time = time.time()

# run code
func_one(10000000)

# current time after running code
end_time = time.time()

# elapsed time
elapsed_time = end_time - start_time
```

Using `timeit` module

```py
import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

timeit.timeit(stmt, setup, number=100000)
```

### Ziping and Unziping files

A zip file is just a compresed file, meaning you can take a
bunch of files and compress them to save space inside of a zip
file

```py
import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')
```

## Web Scraping with Python

### Introduction to web scraping

Web scraping is a general term for techniques involving
automating the gathering of data from a website.

In this section, we will learn how to use Python to conduct web
scraping tasks such as downloading images or information off
a website.

In order to web scrape with Python, we need to understand
the basic concepts of how a website works.

When a browser loads a website, the user gets to see what is known
as the `front-end` of the website.

Main things we need to understand

- Rules of web scraping
- Limitations of web scraping
- Basic HTML and CSS

Rules of web scraping

- Always try to get permission before scraping
- If you make too many scraping attempts or requests, your IP
  address could get blocked
- Some sites automatically block scraping software

Limitations of web scraping

- In general every website is unique, which means every
  web scraping script is unique
- A slight change or update to a website may completely break
  your web scraping script

  Main frontend components of a website

  - HTML
  - CSS
  - JS

For effective basic web scraping, we only need to have a
basic understanding of HTML and CSS

Python can view these HTML and CSS elements programmatically,
and then extract information from the website.

To web scrape with Python, we can use these libraries

- `BeatifulSoup`
- `requests`

These are external libraries outside of Python, so you need
to install them with either `conda` or `pip` at your commandline.

Directly at your command line use

- `pip install requests`
- `pip install lxml`
- `pip install bs4`

### Setting up

- Install the necessary libraries
- Explore how to inspect elements and view source of a webpage

### Grabbing a Title

```py
import requests
import bs4

url = 'https://en.wikipedia.org/wiki/Jonas_Salk'

def grab_title():
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    title = soup.select('title')[0].getText()
    return title
    
if __name__ == '__main__':
    title = grab_title()
    print(title)
```

### Grabbing all elements of a class

We previously mentioned a big part
of web scraping with the BS4 library
is figuring out what string syntax to
pass into the `soup.select()` method.

```py
import requests
import bs4

url = 'https://en.wikipedia.org/wiki/Jonas_Salk'

def grab_classes():
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    
    for item in soup.select('.toctext'):
        yield item.text

if __name__ == '__main__':
    for text in grab_classes():
        print(text)
```

### Grabbing an Image

BeautifulSoup can scan a page, locate the `<img>` tags
and grab these URLs.

Then we can download the URLs as images and write them
to the computer.

```py
import requests
import bs4

url = 'https://en.wikipedia.org/wiki/Jonas_Salk'

def grab_image():
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    for element in soup.select('.thumbimage'):
        src = element['src']
        link = 'https:' + src

        image_link = requests.get(link)

        # raw content of the actual image
        # binary file
        print(image_link.content)

        # save file
        # write binary
        with open('image.jpg', 'wb') as f:
            f.write(image_link.content)

        # only save the first image
        break

if __name__ == '__main__':
    grab_image()
```

### Book examples

Working with multiple pages and items

We've seen how to grab elements one at a time. But
realistically, we want to be able to grab multiple elements,
most likely across multiple pages.

This is where we can combine our prior python
knowledge with the web scraping libraries to create
powerful scripts

We will use a site specifically designed to practice
web scraping: [site](www.toscrape.com)

We will practice grabbing elements across multiple pages.

Get the title of every book with a 2 star rating

```py
import requests
import bs4

def get_book_titles():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

    for page in range(1, 6):
        print('\nScrap Page {}\n'.format(page))

        scrape_url = base_url.format(page)
        response = requests.get(scrape_url)

        soup = bs4.BeautifulSoup(response.text, 'lxml')
        
        counter = 1
        for book_element in iter(soup.select('.product_pod')):
            if len(book_element.select('.star-rating.Two')) > 0:
                book_title = book_element.select('a')[1]['title']
                yield (page, counter, book_title)

                counter += 1

if __name__ == '__main__':
    print('All 2 stars books')
    for page, index, title in get_book_titles():
        print('Page {}: #{} - {}'.format(page, index, title))
```

## Working with Images in Python

In this section we will focus on learning how to
work with images with the `Pillow` library. We'll
install it with `pip install pillow` and then show
you how to open and save image files and interact with
images.

We will use the Pillow library for this,
which is a fork of the `PIL` (Python Imaging Library)
with easy to use function calls.

Install library at your command line with: `pip install pillow`

```py
from PIL import Image

image = Image.open('example.jpg')

print(type(image))
image.show()

print(image.size)
print(image.filename)
print(image.format_description)
```

Perform some operations on image

- `crop`: cropping is just grabbing a subsection
  of the image.

```py
from PIL import Image

image = Image.open('example.jpg')

# crop top left
x = 0
y = 0
w = 120
h = 120

image.crop((x,y,w,h))
image.resize((120,120))
image.rotate(90)

image.save('test.jpg')
```

## Working with PDF and CSV Files

Python has the ability to work with PDF files and
spreadsheet files

### Working with CSV files in Python

CSV stands for comma seperated variables and is a very
common output for spreadsheet programs

Example:

- Name, Hours, Rate
- David, 20, 15
- Claire, 40, 20

Note, that while its possible to export excel files
and Google Spreadsheets to `.csv` files. It only
exports the information.

Things like formulas, images, and macros can not be
within a `.csv` file.

Simply put a `.csv` file only contains the raw data from
the spreadsheet.

We will work with the built-in `csv` module for Python,
which will allow us to grab columns, rows and values from
a `.csv` file as well as write to a `.csv` file. Keep
in mind, this is a very popular space for outside libraries,
which you may want to explore.

Other libraries to consider:

- Pandas:
  - Full data analysis library, can work with almost any
    tabular data type
  - Runs visualizations and analysis
  - One of my personal favorites, we teach it in various
    data science courses

- Openpyxl:
  - Designed specifically for Excel files

- Google Sheets Python API:
  - Direct Python interface for working with Goolge Spreadsheets
  - Allows you to directly make changes to the spreadsheets hosted online
  - More complex syntax, but available in many programming languages

```py
import csv

# Open the file
data = open('example.csv', encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

headers = data_lines[0]
first_data_row = data_lines[1]

# first 5 lines
for line in data_lines[:5]:
    print(line)

# get all emails
all_emails = []

for line in data_lines[1:]:
    all_emails.append(line[3])

# get all fullname
all_fullnames = []

for line in data_lines[1:]:
    all_fullnames.append(line[1] + ' ' + line[2])

# write file
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['names','emails',])

for index,email in enumerate(all_emails):
    csv_writer.writerow([all_fullnames[index], email])

csv_writer.close()
```

### Working with PDF file in Python

PDF stands for Portable Document Format and was
developed by Adobe in the 1990s.

The most important thing to keep in mind is that while
PDFs share the same extensioin and can be viewed
in PDF readers, many PDFs are `not` machine readable through
Python.

Since PDFs mainly encapsulate and display a fixed-layout flat
document, there is no machine readable standard format,
unlike CSV files.

This means that a PDF that was simply scanned is highly
unlikely to be readable by Python.

Addtitions to PDFs such as images, tables, format
adjustments can also render a PDF unreadable by Python.

There are many paid PDF programs that can read and
extract from these files, but we will use the open-source
and free `PyPDF2` library.

Install library: `pip install PyPDF2`

```py
import PyPDF2

# read binary mode
f = open('test.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()

f.close()
```

Write to PDF

```py
import PyPDF2

f = open('test.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)
page_one = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)

# writer binary
pdf_output = open('output.pdf', 'wb')
pdf_writer.write(pdf_output)
```
