# ---------------- IMPORT LIBRARIES ----------------

import numpy as np
import matplotlib.pyplot as plt


# ---------------- FUNCTION DEFINITIONS ----------------

# Main function: f(x) = x²
def f(x):
    return x**2


# Actual derivative: f'(x) = 2x
def actual_derivative(x):
    return 2 * x


# Numerical derivative using Forward Difference Method
def calculate_numerical_derivative(f, x, step):

    return (
        (f(x + step) - f(x))
        / step
    )


# ---------------- MAIN PROGRAM ----------------

# Initialize parameters
point = 2.0

step_sizes = [0.1, 0.01, 0.001]


# Exact derivative
exact_result = actual_derivative(point)

print("True derivative value:", exact_result)

print("\nApproximate Derivatives:\n")


# Approximate derivatives
for step in step_sizes:

    approximate_result = calculate_numerical_derivative(
        f,
        point,
        step
    )

    print(
        f"Using step = {step}: "
        f"Result = {approximate_result}"
    )


# ---------------- VISUALIZATION ----------------

# Generate x-values
x_range = np.linspace(0, 4, 100)


# Plot main function
plt.plot(
    x_range,
    f(x_range),
    label="$x^2$ function"
)


# Mark point (2, 4)
plt.scatter(
    point,
    f(point),
    label="Point (2, 4)"
)


# Add tangent lines
for step in step_sizes:

    # Approximate slope
    slope = calculate_numerical_derivative(
        f,
        point,
        step
    )

    # Tangent line equation
    tangent = (
        slope * (x_range - point)
        + f(point)
    )

    plt.plot(
        x_range,
        tangent,
        linestyle="--",
        label=f"Tangent h={step}"
    )


# ---------------- GRAPH SETTINGS ----------------

plt.title("Numerical Differentiation Experiment")

plt.xlabel("x")

plt.ylabel("f(x)")

plt.legend()

plt.grid(True)

# Display graph
plt.show()
