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
# EXP 4 (1.4) :  Implementing Secant Algorithms in Python AIM: Implementing Secant Algorithms in Python
## Description

![image](https://github.com/user-attachments/assets/978db41a-151b-4711-88f5-59085b379f2e)


## OUTPUT

![image](https://github.com/user-attachments/assets/db65d6b6-dd0f-45ca-8a1e-13b881e58195)


## LEARNING OUTCOME

![image](https://github.com/user-attachments/assets/89db5869-0015-4729-83a9-bc1802997791)

---------------------------------------------------------
# EXP 5 (2.1) : Hands-on interpolation exercises using Python libraries 
## Description

![image](https://github.com/user-attachments/assets/0f682447-384a-4581-9c4f-60f39d0e5829)


## OUTPUT

![image](https://github.com/user-attachments/assets/3d90792f-9394-4420-be48-9db1664be096)


## LEARNING OUTCOME
![image](https://github.com/user-attachments/assets/836dd8c5-54ea-4ee8-96a7-ffb8641f8554)

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
