# Secant Method
define secant_method(func, x0, x1, tol, max_iter)
    initialize x_k_minus_1 to x0
    initialize x_k to x1

    for k from 0 to max_iter - 1
        f_k_minus_1 = func(x_k_minus_1)
        f_k = func(x_k)
        
        x_k_plus_1 = x_k - f_k * (x_k - x_k_minus_1) / (f_k - f_k_minus_1)
        
        if abs(x_k_plus_1 - x_k) < tol
            return x_k_plus_1, k + 1  # Return root and number of iterations
        
        x_k_minus_1 = x_k
        x_k = x_k_plus_1

    raise error "Secant method did not converge"

# Example usage
define target_function(x)
    return x^2 - 4

# Initial guesses
x0 = 1.0
x1 = 3.0

# Call secant_method and print results
root, iterations = secant_method(target_function, x0, x1)
print "Root found:", root
print "Iterations:", iterations
