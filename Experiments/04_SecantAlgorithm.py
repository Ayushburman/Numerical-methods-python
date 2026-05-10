# ---------------- SECANT METHOD ----------------

def secant_method(func, x0, x1, tol=1e-6, max_iter=100):

    # Initial values
    x_k_minus_1 = x0
    x_k = x1

    # Iteration loop
    for k in range(max_iter):

        f_k_minus_1 = func(x_k_minus_1)
        f_k = func(x_k)

        # Prevent division by zero
        if (f_k - f_k_minus_1) == 0:
            raise ZeroDivisionError("Division by zero encountered.")

        # Secant formula
        x_k_plus_1 = x_k - (
            f_k * (x_k - x_k_minus_1)
            / (f_k - f_k_minus_1)
        )

        # Check convergence
        if abs(x_k_plus_1 - x_k) < tol:
            return x_k_plus_1, k + 1

        # Update values
        x_k_minus_1 = x_k
        x_k = x_k_plus_1

    # If method fails
    raise ValueError("Secant method did not converge")


# ---------------- EXAMPLE FUNCTION ----------------

def target_function(x):
    return x**2 - 4


# Initial guesses
x0 = 1.0
x1 = 3.0


# Calling Secant Method
root, iterations = secant_method(
    target_function,
    x0,
    x1
)

# Printing Results
print("Root found:", root)
print("Iterations:", iterations)
