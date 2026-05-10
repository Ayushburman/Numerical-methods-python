from scipy.optimize import minimize

# Objective function to minimize
def objective_function(x):
    return x[0]**2 + x[1]**2

# Equality constraint function
def constraint_equation(x):
    return x[0] + x[1] - 1

# Lagrangian function
def lagrangian(x, lambda_):
    return objective_function(x) + lambda_ * constraint_equation(x)

# Wrapper function for scipy.optimize.minimize
def optimize_with_lagrange(initial_guess):
    result = minimize(lambda x: lagrangian(x, 1.0), initial_guess, constraints={'type': 'eq', 'fun': constraint_equation})
    return result

# Initial guess
initial_guess = [0.5, 0.5]

# Optimize using Lagrange multipliers
result = optimize_with_lagrange(initial_guess)

# Display the results
print("Optimal solution:", result.x)
print("Optimal value:", result.fun)
print("Lagrange multiplier:", result.fun - objective_function(result.x))
