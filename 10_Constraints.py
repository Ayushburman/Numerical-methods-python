# ---------------- IMPORT LIBRARIES ----------------

import numpy as np
from scipy.optimize import minimize


# ---------------- OBJECTIVE FUNCTION ----------------

# f(x, y) = x² + y²
def objective(variables):

    x, y = variables

    return x**2 + y**2


# ---------------- CONSTRAINT FUNCTIONS ----------------

# Equality constraint: x + y = 1
def equality_constraint(variables):

    x, y = variables

    return x + y - 1


# Inequality constraint: x ≥ y
# scipy uses constraint >= 0
def inequality_constraint(variables):

    x, y = variables

    return x - y


# ---------------- MAIN PROGRAM ----------------

# Starting point
initial_guess = [0.5, 0.5]


# Define constraints
constraints = [

    {
        "type": "eq",
        "fun": equality_constraint
    },

    {
        "type": "ineq",
        "fun": inequality_constraint
    }
]


# Solve optimization problem
solution = minimize(
    objective,
    initial_guess,
    constraints=constraints
)


# ---------------- RESULTS ----------------

best_x = solution.x[0]

best_y = solution.x[1]

minimum_value = solution.fun


print("Best x, y values:")

print(f"x = {best_x}")

print(f"y = {best_y}")

print("\nMinimum value:")

print(minimum_value)
