# Python Language Cheat Sheet

Covers Python 3.5, the version that comes with the Rasbian OS.

We link to relevant [Python Docs](https://docs.python.org/3.5/) for more detail:
* [The Python Tutorial](https://docs.python.org/3.5/tutorial/) Introduces Python's most noteworthy features. After reading it, you will be able to read and write Python modules and programs. (start here)
* [Built-in Functions](https://docs.python.org/3.5/library/functions.html) are always available
* [Standard Library](https://docs.python.org/3.5/library/index.html)  a description of standard objects and modules

## Comments

Comments start with a hash, `#`, and go to the end of the line. They explain code, but don't do anything.

```python
# this is the first comment
3 + 3 # and this is the second comment
```

## Numbers

See *[Numbers](https://docs.python.org/3.5/library/stdtypes.html#typesnumeric)*
and *[Using Python as a Calculator](https://docs.python.org/3.5/tutorial/introduction.html#numbers)*

Numeric Data Types:

* Integers are whole numbers (e.g. `1`, `2`, `20`) and have type `int`.
* Floats have a fractional part (e.g. `1.0`, `2.0`, `3.1415926`) and have type `float`.

Arithmetic operations on numbers:

* Addition `3 + 1`
* Subtraction `5 - 1`
* Multiplication `2 * 2`
* Division `8 / 2 = 4.0` returns a float
* Floor division `8 // 2 = 4` returns an integer, discarding the fractional part of the result
* Modulo `a % b` returns the remainder of `a / b`
* Exponentiation `2 ** 3`
* Negation `- 1`

Functions on numbers:

* [`abs(x)`](https://docs.python.org/3.5/library/functions.html#abs)
  absolute value of x.
* [`int(x)`](https://docs.python.org/3.5/library/functions.html#int)
  converts x to an integer.
* [`float(x)`](https://docs.python.org/3.5/library/functions.html#float)
  converts x to a float.
* [`pow(x, y)`](https://docs.python.org/3.5/library/functions.html#pow)
  returns x to the power of y.

## Strings

*[Strings](https://docs.python.org/3.5/tutorial/introduction.html#strings)* can be enclosed in single quotes or double quotes.
Use `\` to escape special characters within the string.

```python
'hello'
"hello"
'don\'t forget to escape' # escape matching quotes within the string
"don't need to escape"    # ...or switch between single and double-quoting
```

Special characters include newline (`\n`), tab (`\t`)

Operations on strings:

* Concatenate `'Raspberry' + 'Pi'`
* Repeat `2 * 'hip ' + 'hooray'`
* Index `'Python'[0]` returns the character at the position (or index) given, starting with `0`.
  Use a negative index, `word[-1]`, to index from the end, starting with `-1`.
* Slice `'one two'[0:3]` returns the substring including the start, but excluding the end.

Functions on strings:

* [`len(str)`](https://docs.python.org/3.5/library/functions.html#len)
  length of the string
* [`str.format()`](https://docs.python.org/3.5/library/string.html#formatstrings)
  format strings
* [`format % values`](https://docs.python.org/3.5/library/stdtypes.html#old-string-formatting)
  old-style string formatting

## Booleans

Either `True` or `False`. Any non-zero value is considered `True`.

Operations on Booleans:

* `a and b` returns `True` if both `a` and `b` are `True`
* `a or b` returns `True` if either `a` or `b` or `True`
* `not a` returns `True` if `a` is `False`

Comparison operators (return a Boolean):

* Greater than `2 > 1`
* Greater than or equal to `a >= b`
* Less than `1 < 2`
* Less than or equal to `a <= b`
* Equality `1 == 1`
* Difference `'apples' != 'oranges'`

Comparisons may be chained together. As in mathematics, operators are evaluated
in order of precedence, but you can always use parenthesis to make it clear.

## Lists

*[Lists](https://docs.python.org/3.5/tutorial/introduction.html#lists)* are a compound data type, used to group other data types together. Lists are mutable, so they can be changed without needing to create a new one.

```python
[1, 2, 3] # values are separated by commas and surrounded by square brackets
['red', 'yellow', 'blue'] # usually items are all the same type
['one', 2, 3.0]  # ...but they can be anything
['four', [5, 6]] # ...even other lists
```

Operations on Lists:

* Concatenate `[1, 2, 3] + [4]`
* Index `[1, 2, 3][0]` returns the item starting with `0`.
  Like strings, a negative number indexes from the end, starting with `-1`.
* Slice `[1, 2, 3][-2:]`

Functions on lists:

* `x.append(3)`
  add a new item to the end of the list
* [`len(x)`](https://docs.python.org/3.5/library/functions.html#len)
  length of the list
* [`min(x)`](https://docs.python.org/3.5/library/functions.html#min)
* [`max(x)`](https://docs.python.org/3.5/library/functions.html#max)

#### range()

See [The Range Function](https://docs.python.org/3.5/tutorial/controlflow.html#the-range-function)

While not a list, a range is like a convenient list-generator. It starts at zero, and stops before the given number.

```python
range(5) # Acts like the list, [0, 1, 2, 3, 4]
```

You can start at a different number.
```python
range(5, 10) # Acts like the list, [5, 6, 7, 8, 9]
```

To print a range, first convert it to a list.
```python
print(list(range(5, 10)))
```

## Other Data Types

Save these for later. They will come up often, but we won't focus on them here.

#### Tuples

Like a list, a tuple is a sequence of values, but they are surrounded by parenthesis. A tuple is immutable.

```python
x = 3
tuple = (1, 2, x) # we can't add or remove items from a tuple
x = 4 # a tuple can contain mutable values. So, we can modify `x`.
```

#### Sets

As in mathematics, a
[set](https://docs.python.org/3.5/tutorial/datastructures.html#sets)
is an unordered sequence of values that is guaranteed to have no duplicate values. It is surrounded by curly brackets, `{}`. Sets support mathematical set operations like union, intersection, and difference.

```python
odd = {1, 3, 5, 7}
even = {2, 4, 6, 8}

odd - even # numbers in odd but not in even (difference)
odd | even # numbers in odd or even (union)
odd & even # numbers in odd and even (intersection)
```

#### Dictionaries

A [dictionary](https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries)
contains key-value pairs. Unlike a sequence, it is indexed by keys instead of numbers.

```python
pie_votes = { 'apple': 31, 'raspberry': 3, 'mud': 0}

apple_votes = pie_votes['apple'] # access items by key
```

## Statements

The statement is followed by a colon, `:`.
The body of statements is indented, which is Python's way of grouping code that goes with the statement.

* [`if`](https://docs.python.org/3.5/tutorial/controlflow.html#if-statements) executes the body only if the condition is true.
  Provide `elif` statements for alternatives with conditions.
  Provide an `else` to run if no other conditions are met.

  ```python
  x = 4
  if x == 1:
    print('x is 1')
  elif x > 10:
    print('x is greater than 10')
  elif x > 20:
    print('will never get here!')
  elif False:
    print('will never get here!')
  else:
    print('ding! ding! ding!')
  ```

* [`while`](https://docs.python.org/3.5/reference/compound_stmts.html#while) loop repeats as long as a condition remains `True`

  ```python
  condition = True
  while condition:
    print(condition)
    condition = False

  while True:
    print('Never Gonna Give You Up')
    print('Never Gonna Let You Down')
  ```

* [`for`](https://docs.python.org/3.5/tutorial/controlflow.html#for-statements) iterates over the elements of a sequence

  ```python
  list = ['get ready', 'get set', 'go!']
  for item in list:
    print(item)
  ```

## Variables

Stores a value and lets you give it a name.

```python
x = 1
x = 'apple'
x = [1, 2, 3]
```

Good variable names are important to clean, readable code.
They should be short and descriptive.
* By convention, we use `_` for variables we don't care about.

## Formatting Output

Python has lots of ways to convert values into strings.

#### Old string formatting

https://docs.python.org/3.5/tutorial/inputoutput.html#old-string-formatting

Substitutes values into a string at `%` placeholders, applying a format. The format determines the type. You can also control the width, precision and length.

Types we'll use:
  * `f` floating point number (a float)
    For floats, precision is the number of digits after the decimal point
  * `i` integer
  * `s` string

```python
import math

'The value of PI is approximately %.2f.' % math.pi  # Floating point number, 2-digits of precision
'The value of PI is approximately %9.2f.' % math.pi # width of 10.

'...or just %i' % math.pi # Integer

'Raspberry %s' % 'pi!' # String

'%i, %i, %.1f, %s!' % (1, 2, 2.5, 'go') # Mix and match multiple values
```

#### Fancy Format Strings

The [str.format()](https://docs.python.org/3.5/library/stdtypes.html#str.format) is great, powerful, and kinda complicated for a beginner.

The format function substitutes values into a string.
```python
from math import pi

"Raspberry {}".format('Pi')
"Pi is {0}, but pie is {1}".format(pi, 'yum!')
```

By providing a format specifier, you get great control over how to format the value. It works better than the old style. The downside is there is an overwhelming amount of flexibility. We won't cover them.

## Functions

As you write longer programs, you'll begin to need a way to re-use bits of code.
*[Defining Functions](https://docs.python.org/3.5/tutorial/controlflow.html#defining-functions)* lets you name a body of code and re-use it by name. Also, it lets you provide parameters each place you use the function.

* Give it a good name.
* Provide names for any parameters (arguments) you will accept. Parameters can have default values.
* Providing a docstring, or [documentation string](https://docs.python.org/3.5/tutorial/controlflow.html#tut-docstrings), is a good habit.
* Use `return` to provide a return value.

```python
def say_something():
  print('something')

say_something()

def to_fahrenheit(celsius): # accepts one parameter, 'celsius'
  """Convert Celsius to Fahrenheit""" # (optional) documentation string
  return celsius * 1.8 + 32

to_fahrenheit(0.0)
```

Function's parameters (arguments) can have default values, making the parameter optional when you use the function. Functions can be called with positional arguments or [keyword arguments](https://docs.python.org/3.5/tutorial/controlflow.html#keyword-arguments).

```python
def say(statement = 'something'): # accepts one parameter, 'statement', with a default value of 'something'
  """Say 'something', or say the provided statement."""
  print(statement)

say('what!') # positional
say(statement='what!') # keyword
```

## Modules

See [*Modules*](https://docs.python.org/3.5/tutorial/modules.html)

To write a longer program, you might split it into several files to keep it organized.
* A *script* is a file of Python that you run.
* A *module* is a file of Python that you *import* to use in a script or another module.
  A module can have sub-modules.

Once you `import` a module, you can use all the functions it provides.

```python
import time # import the time module

time.sleep(1) # access to the functions "through" the imported module
print('The current time is ' + time.strftime('%I:%M:%S %p'))
```

It can look "cleaner" to `import` just the things plan to use `from` a module.

```python
from time import sleep, strftime # import only sleep() and strftime() from the time module

sleep(1) # access the functions directly
print('The current time is ' + strftime('%I:%M:%S %p'))
```

### The Standard Library

Python comes with the [Standard Library](https://docs.python.org/3.5/library/index.html). You can import modules from the Standard Library without downloading or installing anything.

#### Time

```python
from time import time, strftime, sleep

sleep(1)
now = time()
now = strftime('%I:%M:%S %p')
```

[time](https://docs.python.org/3.5/library/time.html) functions:
* [`time()`](https://docs.python.org/3.5/library/time.html#time.time) returns the current system time in seconds since the epoch
* [`sleep(secs)`](https://docs.python.org/3.5/library/time.html#time.time) stops running for the given number of seconds
* [`strftime(format)`](https://docs.python.org/3.5/library/time.html#time.strftime) make a formatted time string

|      | Description |
|------|-------------|
| `%Y` | Full year |
| `%B` | Full month name |
| `%m` | Month (number) |
| `%d` | Day of the month |
| `%I` | Hour (12-hour clock) |
| `%M` | Minute |
| `%S` | Second |
| `%p` | AM or PM |

#### Files

To read and write files, use
[`open(filename, mode)`](https://docs.python.org/3.5/tutorial/inputoutput.html#reading-and-writing-files).

The modes are one of:
* `'r'` only read (default)
* `'w'` only write (erasing any existing file with the same name)
* `'a'` append (add to the end of any existing file)
* `'r+'` both read and write

Append `'b'` for binary mode (`'rb'` for binary read). Use this for non-text files, like images.

```python
with open('data.txt') as f: # Open a file for reading
  data = f.read()           # Read the (text) contents

with open('data.txt', 'w') as f: # Open a file for writing
  f.write('Everybody! Everybody!')
  f.write('Everybody! Lah-dee-dah-dee-dah!')
```

See [Reading and Writing Files](https://docs.python.org/3.5/tutorial/inputoutput.html#reading-and-writing-files) for more file functions: `f.readlines()`, `f.readline()`, `f.write()`.

#### CSV files

CSV is great for writing rows of data. This format is perfect for loading into a spreadsheet.

```python
import csv

temperature_readings = [
  ['2:30 PM', 87.6],
  ['2:40 PM', 87.7],
  ['2:50 PM', 88.0]
]
# Save the readings
with open('temperature_log.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['Time', 'Temperature']) # Column names are helpful
  for time, temp in temperature_readings:
    writer.writerow(time, temp)
```

#### JSON files

JSON files are relatively easy to read, but can handle all sorts of data structure (not just rows and columns like CSV). This format is perfect for communicating data with web services.

```python
import json

temperature_readings: [
  { 'time': '2:30 PM', 'temperature': 87.6 },
  { 'time': '2:40 PM', 'temperature': 87.7 },
  { 'time': '2:50 PM', 'temperature': 88.0 },
]
# Save the readings
with open('temperature_log.json', 'w') as f:
  json.dump(temperature_readings, f)

# Load previous readings
with open('temperature_log.json', 'r') as f:
  temperature_readings = json.load(f)
```

See [Saving structured data with json](https://docs.python.org/3.5/tutorial/inputoutput.html#saving-structured-data-with-json) to learn more. It explains how the [json](https://docs.python.org/3.5/library/json.html#module-json) module takes care of *serializing* your data into a string representation when you save to a file, and *deserializing* the file back into your data when you read.
