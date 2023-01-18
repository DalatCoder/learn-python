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
