# Bisection Method
define bisection_method(func, a, b, tol, max_iter)
    if func(a) * func(b) > 0
        raise error
    initialize iteration to 0
    
    while (b - a) / 2 > tol and iteration < max_iter
        c = (a + b) / 2
        if func(c) == 0
            return c
        else if func(c) * func(a) < 0
            b = c
        else
            a = c
        increment iteration
    
    return (a + b) / 2

# Example usage of Bisection Method
define quadratic_function(x)
    return x^2 - 4
call bisection_method(quadratic_function, 0, 3) and print result

# Newton-Raphson Method
define newton_raphson_method(func, func_derivative, initial_guess, tol, max_iter)
    initialize x to initial_guess
    initialize iteration to 0
    
    while abs(func(x)) > tol and iteration < max_iter
        x = x - func(x) / func_derivative(x)
        increment iteration
    
    return x

# Example usage of Newton-Raphson Method
define cubic_function(x)
    return x^3 - 6*x^2 + 11*x - 6
define cubic_derivative(x)
    return 3*x^2 - 12*x + 11
initial_guess = 1.5
call newton_raphson_method(cubic_function, cubic_derivative, initial_guess) and print result
