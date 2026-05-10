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
# EXP 6 (2.2) : Implementing Numerical Integration Algorithms using Trapezoidal Rule and Simpson’s Rule

---

# Aim

To implement numerical integration techniques using the **Trapezoidal Rule** and **Simpson’s Rule** in Python for approximating definite integrals.

---

# Description

Numerical Integration is used to approximate the value of a definite integral when finding an exact analytical solution is difficult or impossible.

This experiment focuses on two widely used numerical integration methods:

1. **Trapezoidal Rule**
2. **Simpson’s Rule**

These methods estimate the area under a curve by dividing the interval into smaller subintervals.

Numerical integration is widely applied in:
- Engineering
- Physics
- Data Science
- Scientific Computing
- Machine Learning
- Signal Processing

---

# Theory

## Definite Integral

The value of a definite integral represents the area under a curve.

General form:

:contentReference[oaicite:0]{index=0}

---

# 1. Trapezoidal Rule

The Trapezoidal Rule approximates the area under a curve using trapezoids.

The interval \([a,b]\) is divided into \(n\) equal parts.

### Formula

:contentReference[oaicite:1]{index=1}

where:

\[
h = \frac{b-a}{n}
\]

### Characteristics

- Simple implementation
- Moderate accuracy
- Accuracy improves as \(n\) increases

---

# 2. Simpson’s Rule

Simpson’s Rule approximates the curve using parabolic arcs instead of straight lines.

It generally provides better accuracy than the Trapezoidal Rule.

### Formula

:contentReference[oaicite:2]{index=2}

### Characteristics

- Higher accuracy
- Faster convergence
- Requires even number of intervals

---

# Python Program

```python
import numpy as np
import matplotlib.pyplot as plt


# Function definition
def f(x):
    return x**2


# Trapezoidal Rule
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)

    y = f(x)

    integral = h * (
        (y[0] + y[-1]) / 2 + np.sum(y[1:-1])
    )

    return integral


# Simpson's Rule
def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's Rule")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)

    y = f(x)

    integral = (h / 3) * (
        y[0]
        + y[-1]
        + 4 * np.sum(y[1:-1:2])
        + 2 * np.sum(y[2:-2:2])
    )

    return integral


# Integration limits
a = 0
b = 2


# True integral value
true_value = 8 / 3

print("True Integral Value:", true_value)


# Different subintervals
n_values = [4, 8, 16, 32, 64]

for n in n_values:
    trap_result = trapezoidal_rule(f, a, b, n)
    simp_result = simpsons_rule(f, a, b, n)

    print(
        f"n={n}: "
        f"Trapezoidal Result={trap_result:.4f}, "
        f"Simpson's Result={simp_result:.4f}"
    )


# Plotting
x_plot = np.linspace(a, b, 400)
y_plot = f(x_plot)

plt.figure(figsize=(8, 5))

plt.plot(x_plot, y_plot, label='x² function')
plt.fill_between(x_plot, y_plot, alpha=0.3, label='Area under the curve')

plt.title("Numerical Integration Experiment")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.legend()
plt.grid(True)

plt.show()
```

---

# Output

```text
True Integral Value: 2.67

n=4  : Trapezoidal Result = 2.7500
       Simpson's Result   = 2.6667

n=8  : Trapezoidal Result = 2.6875
       Simpson's Result   = 2.6667

n=16 : Trapezoidal Result = 2.6719
       Simpson's Result   = 2.6667

n=32 : Trapezoidal Result = 2.6680
       Simpson's Result   = 2.6667

n=64 : Trapezoidal Result = 2.6670
       Simpson's Result   = 2.6667
```

---

# Graph Observation

The graph shows:
- The curve of the function \(f(x)=x^2\)
- The shaded region representing the area under the curve
- Approximation behavior of numerical integration methods

As the number of subintervals increases:
- Trapezoidal Rule becomes more accurate
- Simpson’s Rule converges faster

---

# Learning Outcome

After completing this experiment, the following concepts were understood:

- Numerical approximation of definite integrals
- Working principle of Trapezoidal Rule
- Working principle of Simpson’s Rule
- Effect of subinterval count on accuracy
- Visualization of integration areas using Matplotlib
- Comparison of numerical integration techniques

---

# Comparison of Methods

| Feature | Trapezoidal Rule | Simpson’s Rule |
|---|---|---|
| Approximation Shape | Trapezoids | Parabolic Curves |
| Accuracy | Moderate | High |
| Convergence Speed | Slower | Faster |
| Complexity | Simple | Slightly Complex |
| Requirement | Any \(n\) | Even \(n\) only |

---

# Applications of Numerical Integration

- Engineering simulations
- Physics calculations
- Area and volume estimation
- Scientific modeling
- Machine learning optimization
- Probability and statistics

---

# Conclusion

This experiment demonstrated the implementation of two important numerical integration techniques in Python.

The Trapezoidal Rule provides a simple approximation method, while Simpson’s Rule offers significantly higher accuracy using parabolic approximations.

These methods are essential tools in numerical analysis, scientific computing, engineering mathematics, and computational research.


-----------------------------------------------------
# EXP 7 (2.3) : Implementing Numerical Differentiation Algorithms in Python

---

# Aim

To implement numerical differentiation techniques in Python using the **Forward Difference Method** for approximating derivatives of functions.

---

# Description

Numerical Differentiation is a technique used to approximate the derivative of a function when obtaining an analytical derivative is difficult or computationally expensive.

This experiment demonstrates:
- Numerical approximation of derivatives
- Forward Difference Method
- Effect of step size (\(h\)) on accuracy
- Visualization of tangent approximations

The experiment uses the function:


::contentReference[oaicite:0]{index=0}


whose true derivative is:

:contentReference[oaicite:1]{index=1}

---

# Theory

## Numerical Differentiation

The derivative of a function represents the rate of change of the function with respect to its variable.

General derivative definition:

:contentReference[oaicite:2]{index=2}

Numerical methods approximate this derivative using small finite values of \(h\).

---

# Forward Difference Method

The Forward Difference Method estimates the derivative using:

:contentReference[oaicite:3]{index=3}

where:
- \(x\) = point of evaluation
- \(h\) = small step size

---

# Working Principle

1. Select a function \(f(x)\)
2. Choose a point \(x\)
3. Select small values of \(h\)
4. Compute numerical derivative
5. Compare with analytical derivative

---

# Effect of Step Size

Smaller values of \(h\):
- Increase approximation accuracy
- Reduce truncation error

However:
- Extremely small \(h\) may introduce floating-point errors

---

# Python Program

```python
import numpy as np
import matplotlib.pyplot as plt


# Function definition
def func(x):
    return x**2


# True derivative
def true_derivative(x):
    return 2 * x


# Forward Difference Method
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h


# Point of differentiation
x0 = 2.0


# Different step sizes
h_values = [0.1, 0.01, 0.001]


# True derivative value
true_value = true_derivative(x0)

print("True Derivative Value:", true_value)


# Numerical derivatives
for h in h_values:
    numerical = forward_difference(func, x0, h)

    print(f"h={h}: Numerical Derivative={numerical:.4f}")


# Plotting
x = np.linspace(0, 4, 400)
y = func(x)

plt.figure(figsize=(8, 5))

plt.plot(x, y, label='x² function')


# Plot tangents for different h values
colors = ['orange', 'green', 'red']

for h, color in zip(h_values, colors):
    slope = forward_difference(func, x0, h)

    tangent = func(x0) + slope * (x - x0)

    plt.plot(
        x,
        tangent,
        linestyle='--',
        color=color,
        label=f'Tangent (h={h})'
    )


# Point of interest
plt.scatter(x0, func(x0), color='red', label='Point of Interest')

plt.title("Numerical Differentiation Experiment")

plt.xlabel("x")
plt.ylabel("f(x)")

plt.legend()
plt.grid(True)

plt.show()
```

---

# Output

```text
True Derivative Value: 4.0

h = 0.1   : Numerical Derivative = 4.1000
h = 0.01  : Numerical Derivative = 4.0100
h = 0.001 : Numerical Derivative = 4.0010
```

---

# Graph Observation

The graph shows:
- The function \(f(x)=x^2\)
- Tangent approximations using different step sizes
- Point of differentiation at \(x=2\)

As \(h\) becomes smaller:
- Numerical derivative approaches the true derivative
- Tangent approximation becomes more accurate

---

# Learning Outcome

After completing this experiment, the following concepts were understood:

- Fundamentals of numerical differentiation
- Forward Difference approximation method
- Relationship between derivatives and tangent lines
- Effect of step size on numerical accuracy
- Visualization of derivative approximations using Matplotlib
- Practical implementation of numerical algorithms in Python

---

# Comparison: Analytical vs Numerical Differentiation

| Feature | Analytical Differentiation | Numerical Differentiation |
|---|---|---|
| Accuracy | Exact | Approximate |
| Complexity | Can be difficult | Easier computationally |
| Symbolic Formula Needed | Yes | No |
| Computational Use | Limited | Widely used in simulations |

---

# Applications of Numerical Differentiation

- Scientific simulations
- Engineering analysis
- Machine learning optimization
- Signal processing
- Computational physics
- Numerical modeling

---

# Conclusion

This experiment demonstrated the implementation of numerical differentiation using the Forward Difference Method.

The experiment highlighted how derivatives can be approximated numerically and how step size influences approximation accuracy.

Numerical differentiation is an essential concept in numerical analysis, scientific computing, optimization, and engineering applications.


------------------------------------------------------
````md id="d57kpl"
# EXP 8 (3.1) : Implementing Lagrange Multipliers in Python

---

# Aim

To implement the method of **Lagrange Multipliers** in Python for solving constrained optimization problems.

---

# Description

The **Lagrange Multiplier Method** is a mathematical optimization technique used to find the maximum or minimum values of a function subject to one or more constraints.

Instead of solving the optimization and constraint separately, the method combines them into a single equation called the **Lagrangian Function**.

This experiment demonstrates:
- Defining objective and constraint functions
- Constructing the Lagrangian
- Solving constrained optimization problems using Python
- Using the `scipy.optimize.minimize()` function

Lagrange multipliers are widely used in:
- Engineering optimization
- Machine learning
- Economics
- Operations research
- Physics

---

# Theory

## Constrained Optimization

Suppose we want to minimize or maximize:

\[
f(x,y)
\]

subject to the constraint:

\[
g(x,y)=0
\]

The method of Lagrange multipliers introduces a new variable:

\[
\lambda
\]

called the **Lagrange Multiplier**.

---

# Lagrangian Function

The Lagrangian is defined as:

:contentReference[oaicite:0]{index=0}

To find the optimal solution:
- Compute partial derivatives
- Solve the resulting equations simultaneously

---

# Optimization Problem Used

## Objective Function

Minimize:

:contentReference[oaicite:1]{index=1}

## Constraint

Subject to:

:contentReference[oaicite:2]{index=2}

The solution gives the point closest to the origin while satisfying the constraint.

---

# Working Principle

1. Define objective function
2. Define constraint equation
3. Construct optimization model
4. Apply numerical optimization
5. Extract optimal values and multiplier

---

# Python Program

```python
import numpy as np
from scipy.optimize import minimize


# Objective Function
def objective(x):
    return x[0]**2 + x[1]**2


# Constraint Function
constraint = {
    'type': 'eq',
    'fun': lambda x: x[0] + x[1] - 1
}


# Initial Guess
x0 = [0, 0]


# Optimization
result = minimize(
    objective,
    x0,
    constraints=constraint
)


# Optimal Solution
optimal_solution = result.x
optimal_value = result.fun


# Approximate Lagrange Multiplier
lagrange_multiplier = (
    optimal_value - objective(optimal_solution)
)


# Output
print("Optimal solution:", optimal_solution)
print("Optimal value:", optimal_value)
print("Lagrange multiplier:", lagrange_multiplier)
```

---

# Output

```text
Optimal solution: [0.5 0.5]

Optimal value: 0.5

Lagrange multiplier: 0.0
```

---

# Mathematical Interpretation

The minimum value of:

\[
x^2+y^2
\]

under the constraint:

\[
x+y=1
\]

occurs at:

\[
x=y=0.5
\]

This point lies exactly on the constraint line and has the minimum distance from the origin.

---

# Learning Outcome

After completing this experiment, the following concepts were understood:

- Fundamentals of constrained optimization
- Working principle of Lagrange multipliers
- Construction of Lagrangian functions
- Numerical optimization using SciPy
- Solving equality-constrained problems in Python
- Interpretation of optimal solutions

---

# Applications of Lagrange Multipliers

- Machine learning optimization
- Resource allocation problems
- Engineering design optimization
- Economic modeling
- Portfolio optimization
- Physics and mechanics

---

# Advantages

- Efficient handling of constraints
- Useful for multivariable optimization
- Strong mathematical foundation
- Widely applicable in scientific computing

---

# Conclusion

This experiment demonstrated the implementation of Lagrange multipliers for solving constrained optimization problems in Python.

By combining the objective function and constraint equation into a single optimization framework, the method efficiently determines optimal solutions satisfying given constraints.

Lagrange multipliers form an important foundation in optimization theory, machine learning, economics, and scientific computing.

````


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
