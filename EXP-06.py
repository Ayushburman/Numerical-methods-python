import numpy as np
import matplotlib.pyplot as plt

# Define the function to integrate
def func(x):
    return x**2

# Trapezoidal Rule Implementation
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    return integral

# Simpson's Rule Implementation
def simpsons_rule(func, a, b, n):
    if n % 2 == 1:
        raise ValueError("n must be even for Simpson's rule.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral

# Define integration bounds and exact integral value for comparison
a, b = 0, 2
true_value = 2.67  # Known integral of x^2 from 0 to 2

print(f'True Integral Value: {true_value}')

# Experiment with different values of n (number of subintervals)
n_values = [4, 8, 16, 32, 64]
for n in n_values:
    trapezoidal_result = trapezoidal_rule(func, a, b, n)
    simpsons_result = simpsons_rule(func, a, b, n)
    

# Plot the function and the area under the curve
x_values = np.linspace(a, b, 100)
plt.plot(x_values, func(x_values), label='$x^2$ function')
plt.fill_between(x_values, func(x_values), alpha=0.2, label='Area under the curve')

# Show the plot and legend
plt.title('Numerical Integration Experiment')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
