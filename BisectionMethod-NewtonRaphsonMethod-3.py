# ---------------- BISECTION METHOD ----------------

def bisection_method(func, a, b, tol=1e-6, max_iter=100):

    # Check if root exists in interval
    if func(a) * func(b) > 0:
        raise ValueError("Function has same signs at endpoints.")

    iteration = 0

    while (b - a) / 2 > tol and iteration < max_iter:

        c = (a + b) / 2

        # Exact root found
        if func(c) == 0:
            return c

        # Root lies in left half
        elif func(c) * func(a) < 0:
            b = c

        # Root lies in right half
        else:
            a = c

        iteration += 1

    return (a + b) / 2


# Example Function: x² - 4
def quadratic_function(x):
    return x**2 - 4


# Calling Bisection Method
bisection_result = bisection_method(quadratic_function, 0, 3)

print("Bisection Method Root:", bisection_result)


# ---------------- NEWTON-RAPHSON METHOD ----------------

def newton_raphson_method(func, func_derivative,
                          initial_guess,
                          tol=1e-6,
                          max_iter=100):

    x = initial_guess
    iteration = 0

    while abs(func(x)) > tol and iteration < max_iter:

        x = x - func(x) / func_derivative(x)

        iteration += 1

    return x


# Example Function: x³ - 6x² + 11x - 6
def cubic_function(x):
    return x**3 - 6*x**2 + 11*x - 6


# Derivative of cubic function
def cubic_derivative(x):
    return 3*x**2 - 12*x + 11


# Initial Guess
initial_guess = 1.5


# Calling Newton-Raphson Method
newton_result = newton_raphson_method(
    cubic_function,
    cubic_derivative,
    initial_guess
)

print("Newton-Raphson Method Root:", newton_result)
