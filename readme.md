# Python

- Programming is the ability to provide a computer, with a set of instructions in a particular language, that it can understand and perform those operations.

<mark>NOTE : Use whitespaces and indentation correctly</mark>

- Python was created by Guido Van Rossum, 1991. (case sensitive language)

- Python is a high level, interpreted, object oriented programming language known for its simplicity and readability. 

- Python is widely used for web development, data analysis and automation.

- Everything in Python is an object.

### Indentation:

- Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python code to use four spaces.

### DataTypes :

- Numbers : Integer(int), Float(float), Complex Numbers
- Sequence : String(str), List(list) and Tuple(tup)
- Dictionary(dict)
- Boolean(bool)
- Set(set)

- List, Dictionary and Set are mutable datatypes, remaining are immutable.

<mark>NOTE : Everything in Python is an Object</mark>

<mark>NOTE :Garbage collection of datatype "number" and "string" is always delayed by python (exception).
            Python waits for sometime for only these two datatypes, wherein user might reuse the same
            data again in the same code. [ Immediate garbage collection does not happen ]
</mark>

### Type casting :

- It is a process of converting one datatype to another.

- There are two types : Implicit conversion and Explicit conversion.

<mark>NOTE : If datatypes are not compatible for conversion, python will throw an error (Type error)</mark>

- Explicit conversion is manually done by developers using Python functions. str(), int(), float() etc..

### Variables:

- Variable is a named place in the memory where a programmer can store data and later retrieve the data using
the variable name.

<mark>NOTE : Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.</mark>

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.


#### Global Variables:

- Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

- Global variables can be used by everyone, both inside of functions and outside.
