# Python Programming - Multithreading, OOP, NumPy and Pandas

[Udemy](https://udemy.com/course/python-programming-basics-multithreading-oop/)

## Why Python?

- Python is a high level programming language developed by Guido
  van Rossum back in 1985 - 1990

- It was designed to be highly readable: it is one of the easiest
  programming languages to start with

Python programming language

- Python is an interpreted programming language
- It means that the code is interpreted and processed at run-time: there is no need for compiling the program
- It is an object oriented programming language: it may encapsulate code iwthin given classes and objects
- Easy to use with all the major databases

Python fundamentals

- Variables, loops and operators
- Functions
- Basic data structures
- Memory management
- Object Oriented Programming (OOP)
- I/O
- Exceptions and errors

Functions

In computer science and programming, a function is a block of
statements that performs a specific task

- `return`: send a specific value (object) back to it's caller
- `yield`: can produce a sequence of values (objects). It can
  resume execution

Function stop with `return`

```py
def producer():
    for num in range(0,10,1):
        if num % 2 == 0:
            return num

print(producer())
```

Using `yield`

```py
def producer():
    for num in range(0,10,1):
        if num % 2 == 0:
            yield num

for n in producer():
    print(n)
```

## Data Structures in Python

### How to measure the running time of algorithms

Running time of algorithms (Complexity theory)

- It is quite hard to define the running time of a given
  algorithm - because it depends on the underlying hardware
- So maybe measuring the running time is not the best option
- Better approach: measure the `number of steps` instead - how many
  steps a given algorithm requires with respect to the input

Ex: we want to sort an array with `N` items. How many steps does
the given sorting algorithm requires?

- `O(1)` - constant running time complexity: these algorithms are
  the fastest approaches: the running time is independent of the
  `N` input (number of items)

  - Ex: we want to `swap` two items with known indexes in a
    given one-dimensional array
  - So if we know the indexes of given items, then basically
    swapping them is quite easy and quite fast

- `O(N)` - linear running time complexity: these algorithms running
  time scale linearly with the `N` input so the running time
  increases linearly with the size of the input. If we have `2x`
  the size of the input then the running time will be `2x` as well.

  - Ex: Using linear search to find an unknown item in a 1D array

- `O(logN)` - logarithmic running time complexity: these algorithm
  running time scale logarithmically with the `N` input so the
  running time increase logarithmically with the size of the input.

  - Ex: if we want to find an unknown item in a `sorted` 1D array (binary search)

### Data structures

- We can store data effieiently with data structures
- But why to bother with data structures in the main?

> Bad programmers worry about the code, good programmers
> worry about data structures and their relationships

- We may have the wrong intuition: we have to use complex
  optimization techniques to make an algorithm faster, etc.

> We can make algorithms faster with proper data structures!!!

- The essence of data structures is that they can store data
  in an efficient manner - opertaions such as insertion or removal

- So data structures have a huge impact on the final running time
  of given softwares and applications

## Memory Management

### Stack and Heap memory?

There are 2 main types of memory:

- Stack memory
- Heap memory

The stack memory (underlying is `stack` data structure)

- The stack memory is a special region in the `RAM` (random
  access memory).

- This is a special data type (stack) that
  store the `active functions` and `local variables` as well.

- This is how Python knows where to return after finish execution
  of a given function

- Small size, fast access, stores function calls and local variables, no fragmentation

The heap memory (nothing concern with the `heap` data structure)

- The heap memory is a special region in the RAM (random
  access memory) as well

- THe size of the heap memory is way larger than that of the stack
  memory (we can store more items)

- `Objects` are store on the heap memory

- Large size, slow access, stores objects, may become fragmented

### Simulation

![Image](assets/stack1.png)

![Image](assets/stack2.png)

![Image](assets/stack3.png)

![Image](assets/stack4.png)

### Garbage Collection (GC)

In Python, we do not have to bother with objects on the `heap`
memory. The garbage collectioin will remove unused objects.

Where there are no active `references` from the `stack` memory to
a given object on the heap - it becomes eligible for garbage
collection. There are several algorithms to handle this problem
and Python uses the so-called `reference counting` approach.

Every variable in Python is a `reference` to an `object`.
A single object may have several references (variable names)

```py
a = ['kenvin', 23, True]
b = a
c = b

# the list object have 3 references
```

In this case, there are 3 references (a, b, c) to the same object
(`list`).

Every object in Python has an extra field - the `reference counter`
that is increased (decreased) when a pointer to the object is
created (removed)

If the reference counter reaches zero, it means that the garbage
collector can `remove that object` from the `heap memory`

The garbage collection is the process that removes unused and
unreferenced objects from the heap

```py
del a
```

The `del` keyword decrements the reference counter (note that there may be other references to the object)

### Revisiting the types of variables

Most of the variables in Python are objects

How to check whether a given variable is an object or not

```py
a = 'Kenvin'
b = 10
c = 34.5
d = False

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# these variables are stored in the heap memory
print(isinstance(a, object)) # true
print(isinstance(b, object)) # true
print(isinstance(c, object)) # true
print(isinstance(d, object)) # true
```

The object is stored on the heap memory, but the variable, so the
reference is stored on the stack memory and of course the
variable on the stack memory is pointing to the object on the
heap memory. And in Python, most of the variables are like this.

### The `==` and the `is` operator

The `==` operator compares the values

````py
a = [10, 'Kevin', True, 35.6]
b = [10, 'Kevin', True, 35.6]

print(a == b) # True

name1 = 'Adam Smith'
name2 = 'Adam Smith'

print(name1 == name2)

The `is` operator compare the memory locations

```py
a = [10, 'Kevin', True, 35.6]
b = [10, 'Kevin', True, 35.6]
c = a

print(a is b) # False
print(c is a) # True
````

### Call by reference and value

There is a crucial difference in programming between
`call-by-reference` and `call-by-value`

`call-by-value`: just a copy of the original variable is passed
so the original variable will not be changed (C, C++, Java).

```py
def change(x):
    # x is a copy of a
    # change x, not a
    x = x + 1

a = 10
change(a)
print(a)
```

`call-by-reference`: the variable itself is passed so the original
variable may be altered

The Python programming language is something different: here we
are using `pass-by-object-reference`. It depends on wheter
the variable is `mutable` or `immutable`

- `int`, `float`, `strings` are `immutable` objects in Python - this is why we are not able to change the values

```py
def change(x):
    x = x + 1

a = 10
change(a)
print(a)
```

- Python is able to change the values of mutable objects. Python
  has something to do with `pass by object reference`

```py
def add_item(l):
    l.append('This is a new item')

my_list = ['kevin', 10, True]
add_item(my_list)

# my_list changed
print(my_list)
```
