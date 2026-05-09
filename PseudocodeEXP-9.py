// Define the function we want to minimize: f(x,y) = x² + y²
FUNCTION objective(x, y):
    RETURN x² + y²

// Define constraint: x + y = 1
FUNCTION equality_constraint(x, y):
    RETURN x + y - 1

// Define constraint: x ≥ y
FUNCTION inequality_constraint(x, y):
    RETURN x - y

// MAIN OPTIMIZATION PROGRAM
BEGIN
    // Set starting point
    SET initial_x = 0.5
    SET initial_y = 0.5

    // Define optimization problem:
    // Minimize: x² + y²
    // Subject to: x + y = 1
    //            x ≥ y

    // Solve optimization problem
    SET constraints = {
        equality: x + y = 1
        inequality: x ≥ y
    }
    
    SET solution = MINIMIZE(
        function: objective
        start_point: [initial_x, initial_y]
        constraints: constraints
    )

    // Show results
    DISPLAY "Best x,y values: " + solution.point
    DISPLAY "Minimum value: " + solution.value
END
