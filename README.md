# Python Numerical Methods — Laboratory Record

> A structured record of experiments covering Python fundamentals, data structures, root-finding algorithms, interpolation, numerical integration, differentiation, and constrained optimization.

---

## Table of Contents

| § | Experiment | Unit |
|---|---|---|
| [1.1](#11--python-basics-data-types-control-structures-functions) | Python Basics — Data Types, Control Structures, Functions | Unit 1 |
| [1.2](#12--data-structures-stack-queue-linked-list) | Data Structures — Stack, Queue, Linked List | Unit 1 |
| [1.3](#13--root-finding--bisection-method--newton-raphson-method) | Root-Finding — Bisection & Newton-Raphson Methods | Unit 1 |
| [1.4](#14--root-finding--secant-method) | Root-Finding — Secant Method | Unit 1 |
| [2.1](#21--interpolation--linear--cubic-spline) | Interpolation — Linear & Cubic Spline | Unit 2 |
| [2.2](#22--numerical-integration--trapezoidal-rule--simpsons-rule) | Numerical Integration — Trapezoidal & Simpson's Rules | Unit 2 |
| [2.3](#23--numerical-differentiation--forward-difference-method) | Numerical Differentiation — Forward Difference Method | Unit 2 |
| [3.1](#31--lagrange-multipliers) | Lagrange Multipliers | Unit 3 |
| [3.2](#32--optimization-with-equality--inequality-constraints) | Optimization — Equality & Inequality Constraints | Unit 3 |
| [3.3](#33--particle-swarm-optimization-pso) | Particle Swarm Optimization (PSO) | Unit 3 |

---

## Unit 1 — Python Fundamentals & Data Structures

---

### §1.1 · Python Basics — Data Types, Control Structures, Functions

**Objective** → Build foundational Python programming skills as a basis for numerical computing.

#### Key Concepts

**Variables & Primitives**
```python
name = "Shashank"
age  = 22
x    = 10        # int
y    = 3.14      # float
z    = 2 + 3j    # complex
```

**Collections**
```python
fruits      = ["apple", "banana", "cherry"]   # list   — ordered, mutable
coordinates = (10, 20)                         # tuple  — ordered, immutable
```

**Control Flow**
```python
# Conditional
if age >= 18:
    print("Adult")

# Iteration — for
for fruit in fruits:
    print(fruit)

# Iteration — while
count = 1
while count <= 5:
    print(count)
    count += 1
```

**Functions**
```python
def greet(name):
    return f"Hello, {name}!"

def introduce(name, age=18):           # default parameter
    print(f"My name is {name} and I am {age} years old.")
```

#### Output
```
Hello, World!
Name: Shashank, Age: 22
Numeric Types: 10  3.14  (2+3j)
Hello, Shashank!
List of fruits: ['apple', 'banana', 'cherry']
Coordinates Tuple: (10, 20)
Adult
apple  banana  cherry
1  2  3  4  5
Square of 4: 16
My name is Shashank and I am 22 years old.
My name is Raj and I am 25 years old.
```

---

### §1.2 · Data Structures — Stack, Queue, Linked List

**Objective** → Implement and demonstrate fundamental linear data structures in Python.

#### 1. Stack · LIFO

```
Top
 ↓
[ 3 | 2 | 1 ]
```

Operations → `push()` · `pop()` · `peek()` · `size()`

```python
class Stack:
    def __init__(self):  self.items = []
    def push(self, item): self.items.append(item)
    def pop(self):        return self.items.pop()
    def peek(self):       return self.items[-1]
    def size(self):       return len(self.items)
```

#### 2. Queue · FIFO

```
Front → [ 1 | 2 | 3 ] → Rear
```

Operations → `enqueue()` · `dequeue()` · `size()`

```python
class Queue:
    def __init__(self):     self.items = []
    def enqueue(self, item): self.items.append(item)
    def dequeue(self):       return self.items.pop(0)
    def size(self):          return len(self.items)
```

#### 3. Linked List · Dynamic Pointers

```
[ 1 ] → [ 2 ] → [ 3 ] → NULL
```

Operations → `append()` · `display()`

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node; return
        last = self.head
        while last.next: last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")
```

#### Output
```
Stack Operations:
Stack: [1, 2, 3]
Pop: 3    Peek: 2    Size: 2

Queue Operations:
Queue: [1, 2, 3]
Dequeue: 1    Size: 2

Linked List Operations:
1 -> 2 -> 3 -> NULL
```

---

### §1.3 · Root-Finding — Bisection Method & Newton-Raphson Method

**Objective** → Implement iterative root-finding algorithms for nonlinear equations.

#### Theory

**Bisection Method**

Given a continuous function where `f(a) · f(b) < 0`, a root exists in `[a, b]`.

```
midpoint  c = (a + b) / 2
```

Interval is halved iteratively until `|b - a| / 2 < tolerance`.

**Newton-Raphson Method**

Starting from an initial guess `x₀`, successive approximations follow:

```
x_(n+1) = x_n  −  f(x_n) / f'(x_n)
```

#### Implementation

```python
def bisection_method(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        print("Bisection method fails."); return None
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:       return c
        elif f(a)*f(c) < 0: b = c
        else:               a = c
    return (a + b) / 2

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        dfx = df(x)
        if dfx == 0: print("Derivative is zero."); return None
        x_new = x - f(x) / dfx
        if abs(x_new - x) < tol: return x_new
        x = x_new
    return None
```

#### Output
```
Bisection Method Root   : 2.000000238418579
Newton-Raphson Root     : 3.0
```

#### Comparison

| Feature | Bisection | Newton-Raphson |
|---|---|---|
| Convergence | Slow | Fast |
| Requires Derivative | No | Yes |
| Accuracy | Moderate | High |
| Stability | Very Stable | Depends on initial guess |

---

### §1.4 · Root-Finding — Secant Method

**Objective** → Implement the Secant Method as a derivative-free alternative to Newton-Raphson.

#### Theory

Given two initial guesses `x₀` and `x₁`, the next approximation is:

```
x₂ = x₁  −  f(x₁) · (x₁ − x₀) / (f(x₁) − f(x₀))
```

Iterations continue until convergence or maximum iterations are reached.

#### Implementation

```python
def secant_method(f, x0, x1, tol=1e-10, max_iter=100):
    iteration = 0
    while iteration < max_iter:
        fx0, fx1 = f(x0), f(x1)
        if fx1 - fx0 == 0:
            print("Division by zero."); return None
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < tol:
            return x2, iteration + 1
        x0, x1 = x1, x2
        iteration += 1
    return None

def f(x): return x**2 - 4

result = secant_method(f, x0=1, x1=3)
```

#### Output
```
Root found : 2.0000000000004996
Iterations : 6
```

#### Comparison

| Method | Requires Derivative | Speed | Stability |
|---|---|---|---|
| Bisection | No | Slow | Very Stable |
| Newton-Raphson | Yes | Very Fast | Initial-guess dependent |
| Secant | No | Fast | Moderately Stable |

---

## Unit 2 — Interpolation, Integration & Differentiation

---

### §2.1 · Interpolation — Linear & Cubic Spline

**Objective** → Estimate intermediate values using Python's SciPy interpolation tools.

#### Theory

Interpolation constructs a function that passes through a set of known data points to estimate values within the dataset range.

**Linear Interpolation** → Connects adjacent points with straight lines. Fast, piecewise, lower smoothness.

**Cubic Spline Interpolation** → Fits smooth cubic polynomials between adjacent points. High smoothness and accuracy.

#### Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 8, 18, 32, 50])

linear_interp = interp1d(x, y, kind='linear')
cubic_interp  = interp1d(x, y, kind='cubic')

x_new    = np.linspace(1, 5, 100)
y_linear = linear_interp(x_new)
y_cubic  = cubic_interp(x_new)
```

#### Comparison

| Feature | Linear | Cubic Spline |
|---|---|---|
| Curve Type | Straight Lines | Smooth Curves |
| Accuracy | Moderate | High |
| Smoothness | Low | Very Smooth |
| Complexity | Simple | Moderate |

---

### §2.2 · Numerical Integration — Trapezoidal Rule & Simpson's Rule

**Objective** → Approximate definite integrals numerically and compare convergence.

#### Theory

**Trapezoidal Rule** — Approximates area using trapezoids:

```
I ≈ h/2 · [ f(x₀) + 2·Σf(xᵢ) + f(xₙ) ]     where  h = (b−a)/n
```

**Simpson's Rule** — Approximates curve with parabolic arcs (requires even `n`):

```
I ≈ h/3 · [ f(x₀) + 4·Σf(x_odd) + 2·Σf(x_even) + f(xₙ) ]
```

#### Implementation

```python
import numpy as np

def f(x): return x**2

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    y = f(np.linspace(a, b, n + 1))
    return h * ((y[0] + y[-1]) / 2 + np.sum(y[1:-1]))

def simpsons_rule(f, a, b, n):
    if n % 2 != 0: raise ValueError("n must be even")
    h = (b - a) / n
    y = f(np.linspace(a, b, n + 1))
    return (h/3) * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))
```

#### Output — Integrating f(x) = x² over [0, 2] · True value: 2.6667

```
n =  4  →  Trapezoidal: 2.7500    Simpson's: 2.6667
n =  8  →  Trapezoidal: 2.6875    Simpson's: 2.6667
n = 16  →  Trapezoidal: 2.6719    Simpson's: 2.6667
n = 32  →  Trapezoidal: 2.6680    Simpson's: 2.6667
n = 64  →  Trapezoidal: 2.6670    Simpson's: 2.6667
```

Simpson's Rule converges exactly at `n = 4` for a polynomial of degree ≤ 3.

#### Comparison

| Feature | Trapezoidal | Simpson's |
|---|---|---|
| Shape | Trapezoids | Parabolic arcs |
| Accuracy | Moderate | High |
| Convergence | Slower | Faster |
| Restriction | Any `n` | Even `n` only |

---

### §2.3 · Numerical Differentiation — Forward Difference Method

**Objective** → Approximate derivatives numerically and observe the effect of step size `h`.

#### Theory

The Forward Difference approximation:

```
f'(x) ≈ [ f(x + h) − f(x) ] / h
```

As `h → 0`, the approximation converges to the true derivative. However, extremely small `h` introduces floating-point round-off errors.

#### Implementation

```python
import numpy as np

def func(x):            return x**2
def true_derivative(x): return 2 * x
def forward_difference(f, x, h): return (f(x + h) - f(x)) / h

x0 = 2.0
for h in [0.1, 0.01, 0.001]:
    print(f"h={h} → {forward_difference(func, x0, h):.4f}")
```

#### Output — True derivative at x = 2.0 is 4.0000

```
h = 0.1   →  4.1000
h = 0.01  →  4.0100
h = 0.001 →  4.0010
```

#### Comparison

| Feature | Analytical | Numerical (Forward Difference) |
|---|---|---|
| Accuracy | Exact | Approximate |
| Formula Required | Yes | No |
| Computational Use | Limited | Widely used in simulation |

---

## Unit 3 — Constrained Optimization

---

### §3.1 · Lagrange Multipliers

**Objective** → Solve constrained optimization problems using the method of Lagrange multipliers.

#### Theory

To minimize `f(x, y)` subject to constraint `g(x, y) = 0`, the Lagrangian is:

```
L(x, y, λ) = f(x, y) − λ · g(x, y)
```

Setting partial derivatives of `L` to zero yields the optimal solution.

**Problem** — Minimize `x² + y²` subject to `x + y = 1`

#### Implementation

```python
import numpy as np
from scipy.optimize import minimize

def objective(x): return x[0]**2 + x[1]**2

constraint = {'type': 'eq', 'fun': lambda x: x[0] + x[1] - 1}

result = minimize(objective, x0=[0, 0], constraints=constraint)
```

#### Output
```
Optimal solution : [0.5  0.5]
Optimal value    : 0.5
```

**Interpretation** → The point `(0.5, 0.5)` lies on the constraint line `x + y = 1` and is the closest point to the origin satisfying the constraint.

---

### §3.2 · Optimization with Equality & Inequality Constraints

**Objective** → Extend constrained optimization to include both equality and inequality constraints simultaneously.

#### Theory

**Equality constraint** → satisfied exactly: `x₁ + x₂ = 1`

**Inequality constraint** → defines a feasible region: `x₁ ≥ x₂`

#### Implementation

```python
from scipy.optimize import minimize

def objective(x): return x[0]**2 + x[1]**2

eq_constraint   = {'type': 'eq',   'fun': lambda x: x[0] + x[1] - 1}
ineq_constraint = {'type': 'ineq', 'fun': lambda x: x[0] - x[1]}

result = minimize(objective, x0=[0, 0],
                  constraints=[eq_constraint, ineq_constraint])
```

#### Output
```
Optimal solution : [0.5  0.5]
Optimal value    : 0.5
```

**Interpretation** → At `x₁ = x₂ = 0.5`, both constraints are satisfied. The inequality `x₁ ≥ x₂` is active at the boundary, confirming the optimizer correctly handled the feasible region.

---

### §3.3 · Particle Swarm Optimization (PSO)

**Objective** → Apply swarm-intelligence-based optimization to a multidimensional benchmark function.

#### Theory

PSO is a population-based metaheuristic inspired by collective animal behavior. Each particle maintains:

- Current position `x`
- Velocity `v`
- Personal best position `p_i`
- Global best position `g`

**Velocity update:**
```
v_(t+1) = w·v_t + c₁·r₁·(p_i − x_t) + c₂·r₂·(g − x_t)
```

**Position update:**
```
x_(t+1) = x_t + v_(t+1)
```

**Objective function** — Sphere Function:
```
f(x) = Σ xᵢ²     global minimum at x = (0, 0, 0)
```

#### Implementation

```python
import numpy as np
from pyswarm import pso

def objective_function(x): return np.sum(x**2)

lb = [-10, -10, -10]
ub = [ 10,  10,  10]

optimal_solution, optimal_value = pso(objective_function, lb, ub)
```

#### Output
```
Stopping search: Swarm best objective change less than 1e-08

Optimal solution : [-3.63e-05   1.12e-04  -2.43e-05]
Optimal value    : 1.43e-08
```

Converged within machine precision of the true minimum `f(0,0,0) = 0`.

#### Comparison — PSO vs Classical Methods

| Feature | Classical Methods | PSO |
|---|---|---|
| Requires Derivatives | Often | No |
| Handles Nonlinearity | Limited | Excellent |
| Global Optimization | Difficult | Strong |
| Multidimensional | Challenging | Efficient |

---

## Summary

| Unit | Topics | Methods |
|---|---|---|
| Unit 1 | Python Basics, Data Structures, Root-Finding | Bisection, Newton-Raphson, Secant |
| Unit 2 | Interpolation, Integration, Differentiation | Linear/Cubic Spline, Trapezoidal, Simpson's, Forward Difference |
| Unit 3 | Constrained & Unconstrained Optimization | Lagrange Multipliers, SciPy `minimize`, PSO |

---

## Libraries Used

```
numpy          scipy          matplotlib          pyswarm
```

---

*Laboratory Record — Numerical Methods with Python*
