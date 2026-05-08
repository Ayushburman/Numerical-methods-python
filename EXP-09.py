from scipy.optimize import minimize

# Objective function to minimize
def objective_function(x):
    return x[0]**2 + x[1]**2

# Equality constraint function
def equality_constraint(x):
    return x[0] + x[1] - 1

# Inequality constraint function
def inequality_constraint(x):
    return x[0] - x[1]

# Initial guess
initial_guess = [0.5, 0.5]

# Define constraints
constraints = [{'type': 'eq', 'fun': equality_constraint}, {'type': 'ineq', 'fun': inequality_constraint}]

# Optimize with equality and inequality constraints
result = minimize(objective_function, initial_guess, constraints=constraints)

# Display the results
print("Optimal solution:", result.x)
print("Optimal value:", result.fun)
