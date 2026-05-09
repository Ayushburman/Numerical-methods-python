# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# ---------------- FUNCTION TO INTEGRATE ----------------

def func(x):
    return x**2


# ---------------- TRAPEZOIDAL RULE ----------------

def trapezoidal_rule(func, a, b, n):

    h = (b - a) / n

    # Generate n+1 points
    x = np.linspace(a, b, n + 1)

    # Evaluate function
    y = func(x)

    # Trapezoidal formula
    integral = h * (
        np.sum(y) - 0.5 * (y[0] + y[-1])
    )

    return integral


# ---------------- SIMPSON'S RULE ----------------

def simpsons_rule(func, a, b, n):

    # n must be even
    if n % 2 != 0:
        raise ValueError("n must be even")

    h = (b - a) / n

    # Generate n+1 points
    x = np.linspace(a, b, n + 1)

    # Evaluate function
    y = func(x)

    # Simpson's formula
    integral = (
        h / 3 * (
            y[0]
            + 4 * np.sum(y[1:-1:2])
            + 2 * np.sum(y[2:-2:2])
            + y[-1]
        )
    )

    return integral


# ---------------- INTEGRATION BOUNDS ----------------

a = 0
b = 2

# Actual integral of x² from 0 to 2
true_value = 8 / 3

print("True Integral Value:", true_value)


# ---------------- EXPERIMENT ----------------

n_values = [4, 8, 16, 32, 64]

print("\nResults:\n")

for n in n_values:

    trapezoidal_result = trapezoidal_rule(func, a, b, n)

    simpsons_result = simpsons_rule(func, a, b, n)

    print(f"n = {n}")

    print("Trapezoidal Rule :", trapezoidal_result)

    print("Simpson's Rule   :", simpsons_result)

    print("-" * 40)


# ---------------- PLOT FUNCTION ----------------

x_values = np.linspace(a, b, 100)

plt.plot(
    x_values,
    func(x_values),
    label="$x^2$ function"
)

# Fill area under curve
plt.fill_between(
    x_values,
    func(x_values),
    alpha=0.3
)

# Graph settings
plt.title("Numerical Integration Experiment")

plt.xlabel("x")

plt.ylabel("f(x)")

plt.legend()

plt.grid(True)

# Display graph
plt.show()
