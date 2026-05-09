# Initialize variables
age = 22
name = "Shashank"

# Print statements
print "Hello, World!"
print "Name: {name}, Age: {age}"

# Numeric data types
num1 = 10      # Integer
num2 = 3.14    # Float
num3 = 2 + 3j  # Complex
print "Numeric Types:", num1, num2, num3

# String
greeting = "Hello, Shashank!"
print greeting

# List
fruits = ["apple", "banana", "cherry"]
print "List of fruits:", fruits

# Tuple
coordinates = (10, 20)
print "Coordinates Tuple:", coordinates

# If statement
if age > 18:
    print "Adult"
else:
    print "Minor"

# For loop
print "Iterating over list of fruits:"
for fruit in fruits:
    print fruit

# While loop
count = 1
print "Counting to 5 using while loop:"
while count <= 5:
    print count
    count = count + 1

# Function definition and call
def greet(name):
    return "Hello, {name}!"
print greet("Shashank")

# Return statement
def square(num):
    return num * num
print "Square of 4:", square(4)

# Default parameters
def introduce(name, age=22):
    print "My name is {name} and I am {age} years old."
introduce("Shashank")
introduce("Raj", 25)
