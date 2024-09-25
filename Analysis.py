# 1. Variables & Data Types:
# What are variables?
# Variables are placeholders for storing data in a program.

# Why do we use variables?
# To store and manage data values in a program, so they can be reused and modified easily.

# How do you create a variable?
# By assigning a value using the = sign. Example: 
x = 5  # stores the value 5 in x

# 2. Data Structures:
# What is a list?
# A list is a collection of items that can be changed.

# Why use a dictionary instead of a list?
# Dictionaries let you store key-value pairs, making it easy to look up values based on a key (like a name or ID).

# How do you create a set?
my_set = {1, 2, 3}  # A set with unique elements.

# 3. Conditional Statements:
# What is an if statement?
# It’s a way to run some code only if a certain condition is true.

# Why use elif and else?
# To handle different conditions and ensure the program responds correctly even if the first condition is false.

# How do you write an if-elif-else structure?
age = 18
if age > 18:
    print("Adult")
elif age == 18:
    print("Just turned 18")
else:
    print("Not an adult")

# 4. Loops:
# What is a for loop?
# It’s used to repeat actions for each item in a sequence (like a list or range of numbers).

# Why use a while loop?
# A while loop keeps running as long as a condition is true, useful when you don’t know in advance how many times the loop should run.

# How do you stop a while loop?
while True:
    print("Looping...")
    break  # Stops the loop.

# 5. Functions:
# What is a function?
# A function is a block of reusable code that performs a specific task.

# Why use functions?
# To avoid writing the same code multiple times, making the program organized and easy to manage.

# How do you define a function?
def greet(name):
    return f"Hello, {name}"

# 6. Exception Handling:
# What is exception handling?
# It’s a way to catch and manage errors during the execution of a program.

# Why handle exceptions?
# To prevent the program from crashing when unexpected errors occur, and to handle them gracefully.

# How do you use try-except?
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 7. File Handling:
# What is file handling?
# It refers to reading from and writing to files stored on your computer.

# Why is file handling important?
# It allows programs to save data, read existing data, and make changes to files.

# How do you read a file?
with open("file.txt", "r") as file:
    content = file.read()

# 8. Importing Libraries:
# What is a library?
# A library is a collection of pre-written code that you can use in your programs.

# Why import libraries?
# To reuse well-tested code, saving time and effort.

# How do you import a library?
import math
print(math.sqrt(16))

# 9. List Comprehension:
# What is list comprehension?
# It’s a shorthand way to create lists in Python.

# Why use list comprehension?
# To write cleaner and more readable code when generating lists from existing data.

# How do you use list comprehension?
squares = [x**2 for x in range(10)]

# 10. Classes & Objects:
# What is a class?
# A class is a blueprint for creating objects, which are instances of that class.

# Why use classes?
# To model real-world things in a program and group related data and functions together.

# How do you define a class?
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# This is a Python class definition for a Person object.

# The __init__ method is a special method in Python classes, known as a constructor.

#  It is automatically called when a new instance (object) of the class is created . 

# The purpose of the __init__ method is to initialize the object's attributes and perform any other setup necessary when an object is instantiated. 

# In this example, the __init__ method initializes the name and age attributes of the Person class.


# 11. Modules:
# What is a module?
# A module is a file containing Python code, such as functions and variables, that you can reuse.

# Why use modules?
# To organize code into separate files and avoid clutter in a single program.

# How do you import a module?
import my_module
my_module.some_function()

# 12. Lambda Functions:
# What is a lambda function?
# A lambda function is a short, anonymous function that you can define in a single line.

# Why use lambda functions?
# To write quick, simple functions without the need to formally define them with def.

# How do you create a lambda function?
double = lambda x: x * 2
print(double(5))

# 13. Common Built-in Functions:
# What is the print() function?
# print() displays output to the console or screen.

# Why use the len() function?
# To find out how many items are in a list or how many characters are in a string.

# How do you use the input() function?
name = input("Enter your name: ")
print(f"Hello, {name}")
