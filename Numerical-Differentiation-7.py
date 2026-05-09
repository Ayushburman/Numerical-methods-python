# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# ---------------- FUNCTION ----------------

def f(x):
    return x**2


# ---------------- ACTUAL DERIVATIVE ----------------

def actual_derivative(x):
    return 2 * x


# ---------------- NUMERICAL DERIVATIVE ----------------

def calculate_derivative(f, x, step_size):

    return (
        (f(x + step_size) - f(x))
        / step_size
    )


# ---------------- MAIN PROGRAM ----------------

# Test point
test_point = 2.0

# Different step sizes
step_sizes = [0.1, 0.01, 0.001]

# True derivative
true_result = actual_derivative(test_point)

print("True Derivative at x = 2:", true_result)

print("\nApproximated Derivatives:\n")

# Test approximations
for step in step_sizes:

    approximated_derivative = calculate_derivative(
        f,
        test_point,
        step
    )

    print(
        f"Step Size = {step}  -->  "
        f"Approx Derivative = {approximated_derivative}"
    )


# ---------------- VISUALIZATION ----------------

# Generate x-values
x_values = np.linspace(0, 4, 200)

# Plot original function
plt.plot(
    x_values,
    f(x_values),
    label="$f(x)=x^2$"
)

# Mark point (2, f(2))
plt.scatter(
    test_point,
    f(test_point)
)

# Tangent line plotting
for step in step_sizes:

    # Approx slope
    slope = calculate_derivative(
        f,
        test_point,
        step
    )

    # Tangent line equation
    tangent_line = (
        slope * (x_values - test_point)
        + f(test_point)
    )

    plt.plot(
        x_values,
        tangent_line,
        label=f"Tangent h={step}"
    )


# ---------------- GRAPH SETTINGS ----------------

plt.title("Numerical Differentiation")

plt.xlabel("x")

plt.ylabel("f(x)")

plt.legend()

plt.grid(True)

# Display graph
plt.show()
