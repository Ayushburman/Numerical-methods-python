# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define function to integrate
define func(x)
    return x^2

# Trapezoidal Rule Implementation
define trapezoidal_rule(func, a, b, n)
    h = (b - a) / n
    x = generate n+1 points between a and b
    y = func(x)
    integral = h * (sum(y) - 0.5 * (y[0] + y[-1]))
    return integral

# Simpson's Rule Implementation
define simpsons_rule(func, a, b, n)
    if n is odd
        raise error "n must be even"
    h = (b - a) / n
    x = generate n+1 points between a and b
    y = func(x)
    integral = h / 3 * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])
    return integral

# Define integration bounds
a = 0
b = 2
true_value = 2.67  # Known integral of x^2 from 0 to 2

print "True Integral Value:", true_value

# Experiment with different values of n
n_values = [4, 8, 16, 32, 64]
for n in n_values
    trapezoidal_result = trapezoidal_rule(func, a, b, n)
    simpsons_result = simpsons_rule(func, a, b, n)
    
# Plot the function and area under the curve
x_values = generate 100 points between a and b
plot(x_values, func(x_values), label="$x^2$ function")
fill area under the curve

# Show the plot and legend
set title "Numerical Integration Experiment"
set xlabel "x"
set ylabel "f(x)"
add legend
display plot
