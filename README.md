# EXP 1 (1.1) : Review of Python Basics, Data Types, Control Structures, and Functions in Python

---

# Description

This experiment provides an introduction to the fundamental concepts of Python programming.  
It covers Python basics, commonly used data types, control structures, and functions.  
The objective of this experiment is to build a strong foundation for advanced programming and numerical methods using Python.

---

# Theory

## 1. Python Basics

Python is a high-level, interpreted programming language known for its simple syntax and readability.

### Key Concepts

- **Variables**  
  Variables are used to store data values dynamically.

  ```python
  name = "Shashank"
  age = 22
  ```

- **Print Statement**  
  Used to display output on the console.

  ```python
  print("Hello, World!")
  ```

- **Comments**  
  Comments are ignored by the Python interpreter and are used to improve code readability.

  ```python
  # This is a comment
  ```

---

## 2. Data Types

Python supports multiple built-in data types.

### Numeric Types

```python
x = 10        # Integer
y = 3.14      # Float
z = 2 + 3j    # Complex
```

### String

A sequence of characters enclosed within quotes.

```python
name = "Shashank"
```

### List

An ordered and mutable collection.

```python
fruits = ["apple", "banana", "cherry"]
```

### Tuple

An ordered but immutable collection.

```python
coordinates = (10, 20)
```

---

## 3. Control Structures

Control structures help in decision-making and repetition.

### If Statement

Used for conditional execution.

```python
age = 22

if age >= 18:
    print("Adult")
```

### For Loop

Used for iterating over sequences.

```python
for fruit in fruits:
    print(fruit)
```

### While Loop

Executes repeatedly while the condition remains true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 4. Functions

Functions are reusable blocks of code designed to perform specific tasks.

### Function Definition

```python
def greet(name):
    return f"Hello, {name}!"
```

### Function Call

```python
print(greet("Shashank"))
```

### Default Parameters

```python
def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")
```

---

# Output

```text
Hello, World!

Name: Shashank, Age: 22
Numeric Types: 10 3.14 (2+3j)

Hello, Shashank!

List of fruits:
['apple', 'banana', 'cherry']

Coordinates Tuple:
(10, 20)

Adult

Iterating over list of fruits:
apple
banana
cherry

Counting to 5 using while loop:
1
2
3
4
5

Hello, Shashank!

Square of 4: 16

My name is Shashank and I am 22 years old.
My name is Raj and I am 25 years old.
```

---

# EXP 2 (1.2) : Implementations of Different Data Structures in Python

---

# Description

This experiment demonstrates the implementation of fundamental data structures using Python.  
The program includes implementations of:

- Stack
- Queue
- Linked List

Each data structure is implemented with its basic operations and demonstrated with sample outputs.

The objective of this experiment is to understand how different data structures organize, store, and manage data efficiently.

---

# Theory

## 1. Stack

A **Stack** is a linear data structure that follows the **LIFO (Last In First Out)** principle.

### Operations Performed

- `push()` → Adds an element to the top
- `pop()` → Removes the top element
- `peek()` → Displays the top element
- `size()` → Returns the number of elements

### Example

```python
stack = [1, 2, 3]
```

Visualization:

```text
Top
 ↓
[1, 2, 3]
```

---

## 2. Queue

A **Queue** is a linear data structure that follows the **FIFO (First In First Out)** principle.

### Operations Performed

- `enqueue()` → Inserts an element
- `dequeue()` → Removes the first element
- `size()` → Returns queue size

### Example

```python
queue = [1, 2, 3]
```

Visualization:

```text
Front → [1, 2, 3] → Rear
```

---

## 3. Linked List

A **Linked List** is a dynamic linear data structure where elements are connected using pointers.

Each node contains:
- Data
- Reference to next node

### Operations Performed

- `append()` → Adds a node at the end
- `display()` → Displays all nodes

### Visualization

```text
[1] → [2] → [3] → NULL
```

---

# Python Program

```python
# Stack Implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# Queue Implementation
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Implementation
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("NULL")


# Stack Operations
print("Stack Operations:")

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Pop:", stack.pop())
print("Peek:", stack.peek())
print("Stack size:", stack.size())


# Queue Operations
print("\nQueue Operations:")

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)
print("Dequeue:", queue.dequeue())
print("Queue size:", queue.size())


# Linked List Operations
print("\nLinked List Operations:")

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()
```

---

# Output

```text
Stack Operations:
Stack: [1, 2, 3]
Pop: 3
Peek: 2
Stack size: 2

Queue Operations:
Queue: [1, 2, 3]
Dequeue: 1
Queue size: 2

Linked List Operations:
1 -> 2 -> 3 -> NULL
```

---

# Learning Outcome

After completing this experiment, the following concepts were understood:

- Working of Stack using LIFO principle
- Working of Queue using FIFO principle
- Dynamic memory structure of Linked List
- Basic operations of linear data structures
- Data insertion and deletion techniques
- Practical implementation of data structures using Python

---

# Conclusion

This experiment provided practical understanding of fundamental data structures in Python.  
Stacks, Queues, and Linked Lists are important building blocks used in algorithms, operating systems, databases, compilers, and software development.

Understanding these data structures is essential for mastering Data Structures and Algorithms (DSA).



-----------------------------------------------------
````md id="m48pzc"
# EXP 3 (1.3) : Implementing Root-Finding Algorithms (Bisection Method and Newton-Raphson Method) in Python

---

# Description

Root-finding algorithms are numerical techniques used to determine the values of \(x\) for which:

:contentReference[oaicite:0]{index=0}

These values are called the **roots** or **zeros** of the function.

This experiment focuses on two important numerical methods:

1. **Bisection Method**
2. **Newton-Raphson Method**

These methods are widely used in scientific computing, engineering mathematics, optimization, and numerical analysis.

---

# Theory

## 1. Bisection Method

The **Bisection Method** is an iterative root-finding technique that repeatedly divides an interval into two halves to locate the root.

### Working Principle

If a continuous function changes sign over an interval \([a,b]\), then a root exists between \(a\) and \(b\).

Mathematically:

\[
f(a)\cdot f(b) < 0
\]

The midpoint is calculated as:

:contentReference[oaicite:1]{index=1}

The interval containing the root is selected repeatedly until sufficient accuracy is achieved.

### Advantages

- Simple and reliable
- Guaranteed convergence for continuous functions

### Disadvantages

- Slower convergence compared to other methods

---

## 2. Newton-Raphson Method

The **Newton-Raphson Method** is a fast iterative technique that uses derivatives to approximate roots.

Starting from an initial guess \(x_0\), the next approximation is computed using:

:contentReference[oaicite:2]{index=2}

### Working Principle

- Start with an initial estimate
- Compute function value and derivative
- Update the estimate iteratively
- Repeat until convergence

### Advantages

- Very fast convergence
- High accuracy

### Disadvantages

- Requires derivative calculation
- May fail for poor initial guesses

---

# Python Program

```python
# Bisection Method
def bisection_method(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None

    while (b - a) / 2 > tol:
        c = (a + b) / 2

        if f(c) == 0:
            return c

        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# Newton-Raphson Method
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Derivative is zero.")
            return None

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    print("Maximum iterations reached.")
    return None


# Function for Bisection Method
def f1(x):
    return x**2 - 4


# Function and derivative for Newton-Raphson Method
def f2(x):
    return x**2 - 9


def df2(x):
    return 2 * x


# Using Bisection Method
root_bisection = bisection_method(f1, 0, 3)

# Using Newton-Raphson Method
root_newton = newton_raphson(f2, df2, 5)


# Display Results
print("Bisection Method Root:", root_bisection)
print("Newton-Raphson Method Root:", root_newton)
```

---

# Output

```text
Bisection Method Root: 2.000000238418579
Newton-Raphson Method Root: 3.0
```

---

# Learning Outcome

After completing this experiment, the following concepts were understood:

- Fundamentals of root-finding algorithms
- Working principle of the Bisection Method
- Newton-Raphson iterative approximation technique
- Importance of derivatives in numerical computation
- Accuracy and convergence of iterative methods
- Implementation of numerical algorithms using Python

---

# Comparison of Methods

| Feature | Bisection Method | Newton-Raphson Method |
|---|---|---|
| Convergence Speed | Slow | Fast |
| Requires Derivative | No | Yes |
| Accuracy | Moderate | High |
| Stability | Very Stable | Depends on initial guess |
| Complexity | Simple | Slightly Complex |

---

# Conclusion

This experiment demonstrated two important numerical root-finding techniques used in computational mathematics.

The **Bisection Method** provides reliable convergence through interval halving, while the **Newton-Raphson Method** achieves faster convergence using derivatives.

These methods form the foundation of advanced numerical analysis, optimization algorithms, scientific simulations, and engineering computations.

````


---------------------------------------------------------------
````md id="k39vxn"
# EXP 4 (1.4) : Implementing Secant Algorithm in Python

---

# Aim

To implement the **Secant Method** in Python for finding the roots of nonlinear equations using iterative numerical techniques.

---

# Description

The **Secant Method** is an iterative numerical root-finding algorithm used to approximate the roots of equations.

Unlike the Newton-Raphson Method, the Secant Method does **not require derivatives**.  
Instead, it approximates the derivative using two initial guesses and draws a secant line between them.

The point where the secant line intersects the x-axis becomes the next approximation of the root.

The Secant Method is generally faster than the Bisection Method and computationally simpler than the Newton-Raphson Method.

---

# Theory

## Secant Method

The Secant Method is based on successive approximations using two nearby points.

Given two initial guesses:

\[
x_0 \quad \text{and} \quad x_1
\]

the next approximation is computed using:

:contentReference[oaicite:0]{index=0}

The iterations continue until:
- the approximation error becomes very small, or
- the maximum number of iterations is reached.

---

# Working Principle

1. Select two initial approximations \(x_0\) and \(x_1\)
2. Evaluate the function values
3. Construct a secant line between the points
4. Compute the next approximation
5. Repeat until convergence

---

# Advantages

- Faster convergence than Bisection Method
- Does not require derivative calculation
- Simple implementation

---

# Disadvantages

- Convergence is not always guaranteed
- Sensitive to poor initial guesses
- Can fail if denominator becomes zero

---

# Python Program

```python
def secant_method(f, x0, x1, tol=1e-10, max_iter=100):
    iteration = 0

    while iteration < max_iter:
        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            print("Division by zero error.")
            return None

        # Secant Formula
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        # Check convergence
        if abs(x2 - x1) < tol:
            return x2, iteration + 1

        x0 = x1
        x1 = x2

        iteration += 1

    print("Maximum iterations reached.")
    return None


# Function definition
def f(x):
    return x**2 - 4


# Initial guesses
x0 = 1
x1 = 3


# Calling Secant Method
result = secant_method(f, x0, x1)


# Output
if result:
    root, iterations = result
    print("Root found:", root)
    print("Iterations:", iterations)
```

---

# Output

```text
Root found: 2.0000000000004996
Iterations: 6
```

---

# Learning Outcome

After completing this experiment, the following concepts were understood:

- Working principle of the Secant Method
- Derivative-free root-finding techniques
- Iterative approximation methods
- Convergence behavior of numerical algorithms
- Importance of tolerance and iteration limits
- Python implementation of numerical methods

---

# Comparison with Other Root-Finding Methods

| Method | Requires Derivative | Speed | Stability |
|---|---|---|
| Bisection Method | No | Slow | Very Stable |
| Newton-Raphson Method | Yes | Very Fast | Depends on initial guess |
| Secant Method | No | Fast | Moderately Stable |

---

# Conclusion

This experiment demonstrated the implementation of the Secant Method for solving nonlinear equations numerically.

The Secant Method provides a good balance between computational efficiency and implementation simplicity since it avoids derivative calculations while still converging rapidly in many practical cases.

It is widely used in numerical analysis, scientific computing, engineering mathematics, and optimization problems.

````


---------------------------------------------------------
````md id="p72xla"
# EXP 5 (2.1) : Hands-on Interpolation Exercises Using Python Libraries

---

# Aim

To perform interpolation techniques using Python libraries such as NumPy, SciPy, and Matplotlib for estimating intermediate data values.

---

# Description

Interpolation is a mathematical technique used to estimate unknown values between known data points.

It is widely used in:
- Data Analysis
- Engineering
- Scientific Computing
- Machine Learning
- Signal Processing

In Python, libraries such as **NumPy** and **SciPy** provide efficient tools for performing interpolation operations.

### Libraries Used

- **NumPy**  
  Used for numerical computations and array handling.

- **SciPy**  
  Provides advanced mathematical functions including interpolation methods.

- **Matplotlib**  
  Used for plotting and visualizing interpolation curves.

---

# Theory

## What is Interpolation?

Interpolation estimates values inside the range of a known dataset.

Suppose we know:

| x | y |
|---|---|
| 1 | 2 |
| 2 | 8 |
| 3 | 18 |

Interpolation helps estimate values between these points.

---

# Types of Interpolation Used

---

## 1. Linear Interpolation

Linear interpolation connects data points using straight lines.

It is simple and computationally efficient.

### Formula

:contentReference[oaicite:0]{index=0}

### Characteristics

- Fast computation
- Piecewise linear approximation
- Less smooth output

---

## 2. Cubic Spline Interpolation

Cubic spline interpolation fits smooth cubic curves between data points.

It provides smoother and more accurate interpolation.

### Characteristics

- Smooth continuous curve
- Better approximation
- Widely used in scientific applications

---

# Python Program

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# Original Data Points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 8, 18, 32, 50])


# Creating interpolation functions
linear_interp = interp1d(x, y, kind='linear')
cubic_interp = interp1d(x, y, kind='cubic')


# Generating smooth x values
x_new = np.linspace(1, 5, 100)


# Interpolated values
y_linear = linear_interp(x_new)
y_cubic = cubic_interp(x_new)


# Plotting
plt.figure(figsize=(8, 5))

plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_new, y_linear, label='Linear Interpolation')
plt.plot(x_new, y_cubic, label='Cubic Spline Interpolation')

plt.title("Interpolation Exercise")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.grid(True)

plt.show()
```

---

# Output

## Interpolation Graph

- Blue dots represent original data points
- Linear interpolation creates straight-line connections
- Cubic spline interpolation creates smooth curves

The graph demonstrates how interpolation estimates intermediate values between known points.

---

# Learning Outcome

After completing this experiment, the following concepts were understood:

- Fundamentals of interpolation techniques
- Difference between linear and cubic interpolation
- Use of SciPy interpolation functions
- Data visualization using Matplotlib
- Estimating intermediate data values
- Practical applications of interpolation in scientific computing

---

# Comparison of Interpolation Methods

| Feature | Linear Interpolation | Cubic Spline Interpolation |
|---|---|---|
| Curve Type | Straight Lines | Smooth Curves |
| Accuracy | Moderate | High |
| Smoothness | Low | Very Smooth |
| Complexity | Simple | More Advanced |
| Computational Cost | Low | Moderate |

---

# Applications of Interpolation

- Data smoothing
- Image processing
- Computer graphics
- Weather prediction
- Signal reconstruction
- Engineering simulations
- Scientific data analysis

---

# Conclusion

This experiment demonstrated the implementation of interpolation techniques using Python scientific libraries.

Linear interpolation provides a simple approximation method, while cubic spline interpolation generates smoother and more accurate curves.

Interpolation is an important numerical method widely used in engineering, machine learning, data science, and scientific research.

````


---------------------------------------------------------
# EXP 6 (2.2) :  implementing two common numerical integration algorithms, the trapezoidal rule and Simpson's rule
## Description

![image](https://github.com/user-attachments/assets/216726ad-4ebb-4690-a103-b1b088260b47)


## OUTPUT

![image](https://github.com/user-attachments/assets/c0410925-cd26-4faf-9ded-addda625b142)


## LEARNING OUTCOME

![image](https://github.com/user-attachments/assets/784d0e5f-3d34-41fe-8868-5ce97607e6ba)

-----------------------------------------------------
# EXP 7 (2.3) :  Implementing numerical differentiation algorithms , hands-on experiment implementing numerical differentiation in Python.

## Description

![image](https://github.com/user-attachments/assets/f378a80e-1de1-4ef4-b4a6-96d2ed25ae29)

## OUTPUT

![image](https://github.com/user-attachments/assets/234916b7-beab-43fb-a43e-886fbb6fd693)


## LEARNING OUTCOME

![image](https://github.com/user-attachments/assets/3b4bec82-80fe-41c6-b8a3-c1a92ebc9fbf)

------------------------------------------------------
# EXP 8 (3.1) :  Write a program on Lagrange Multipliers in Python AIM: To implement procedures of Lagrange Multipliers in Python.
## Description

![image](https://github.com/user-attachments/assets/5db42b3e-97c9-4283-95f3-e7779d0d48bc)


## OUTPUT

![image](https://github.com/user-attachments/assets/d3dba1e2-8b31-4394-8c33-66d322422ec7)


## LEARNING OUTCOME

![image](https://github.com/user-attachments/assets/8c94e297-fbed-4017-a6ff-e1e80589a382)

---------------------------------------------------
# EXP 9 (3.2) : Write a program on Optimization with Equality and Inequality Constraints Using Python.
## Description

![image](https://github.com/user-attachments/assets/0a9e06b3-0995-4eb9-9028-9739862b8c0c)


## OUTPUT

![image](https://github.com/user-attachments/assets/e8c081aa-e1f7-4da1-9111-55192fb8ae7f)


## LEARNING OUTCOME

![image](https://github.com/user-attachments/assets/581f0e11-dbf7-40a4-b181-0e8b58421acb)

---------------------------------------------------
# EXP 10 (3.3) : Write a program to Optimization of a Multidimensional Function Using Particle Swarm Optimization in Python
## Description

![image](https://github.com/user-attachments/assets/1b24e15c-5047-4259-bd60-0d41c0cdc2e6)

## OUTPUT

![image](https://github.com/user-attachments/assets/05853f1f-e330-411f-bedc-8268f09f879c)

## LEARNING OUTCOME

![image](https://github.com/user-attachments/assets/8228ff10-42ec-4c6b-8083-690f1da51445)

--------------------------------------------------
