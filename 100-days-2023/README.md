# 100 Days of Code: The Complete Python Pro Bootcamp for 2023

[Course link](https://udemy.com/course/100-days-of-code/)

100 Days of Python Pledge

I Hieu am committed to completing the 100 days of Python challenge.

I hereby pledge to work for at least an hour on Python programming for 100 days.

I will keep myself on track, even though some days I might feel tired or frustrated.

I will keep myself accountable, even though I have lots of things to do, I will make this a priority in my life.

I will overcome difficulties and achieve my goal.

I will become a Python developer.

I believe in myself.

Date: 19/01/2022 - 12:30 PM

## Day 1: Beginner - Working with Variables in Python to Manage Data

Day 1 Goals:

- Printing
- Commenting
- Debugging
- String manipulation
- Variables
- Project: Band Name Generator

### String and Print

```py
print("Hello World!")
print("Hello World!\nHello World!")
```

String concatenation

```py
print('Hello' + ' ' + 'World')
```

### Input function

```py
print('Hello' + ' ' + input('What is your name?') + '!')
```

Beginner Python IDE: [Thonny](https://thonny.org/)

### Comment

```py
# this is a comment
'''
This is a multiple comment
'''
```

### Python variables

```py
name = input('What is your name?')
print(name)
```

### Project: Band Name Generator

```py
print('Welcome to the Band Name Generator')

city_name = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
band_name = city_name + ' ' + pet_name

print('Your band name could be ' + band_name)
```

## Day 2: Beginner - Understanding Data Types

Day 2 goals:

- Data Types
- Numbers
- Operations
- Type Conversion
- `f`-Strings
- Project: Tip Calculator

### Python Primitive Data Types

- String: slices of characters, support indexing
- Integer
- Float
- Boolean

For string and subscripting string

```py
word = 'hello world'

# subscript string
first_letter = word[0]
the_rest = word[1:]
```

Large integers

```py
num = 11
num = 3

large_number = 342_654_896
```

### Type Error, Type Checking and Type Conversion

Get type of a variable with `type()` | Type Checking

```py
a = 1
s = 'hello'
b = True

print(type(a))
print(type(s))
print(type(b))
```

Type Conversion to convert 1 type to another type

```py
a = 1
s = str(a)

print(type(a))
print(type(s))
```

### Mathematical Operations in Python

- `+`
- `-`
- `*`
- `/`: get `float`
- `**`: power

### Number Manipulation and F Strings in Python

```py
result_div = 7 // 2 # div
result_mod = 7 % 2 # mod

score = 10
print('your score is ' + str(score))
print(f'your score is {score}')
print('your score is {}'.format(score))
```

### Project: Tip Calculator

```py
print('Welcome to the tip calculator!')

bill = input('What was the total bill? $')
bill = float(bill)

tip = input('How much tip would you like to give? 10, 12, or 15? ')
tip = int(tip)

people = input('How many people to split the bill? ')
people = int(people)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)
print(f'Each person should pay: {final_amount}')
```

## Day 3: Beginner- Control Flow and Logical Operators

Day 3 goals:

- Conditional Statements
- Logical Operators
- Code Block
- Scope

### Control Flow

```py
if condition:
    # do this
    pass
elif condition:
    # do this
    pass
else:
    # do this
    pass
```

Comparison operators

- `>`
- `<`
- `>=`
- `<=`
- `==`
- `!=`

### Logical Operators

- `A and B`
- `C or D`
- `not E`

### Project: Treasure Island

```py
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
```
