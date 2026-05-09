// Required libraries for math operations and plotting
IMPORT numerical_library
IMPORT plotting_library

// Define main function f(x) = x²
FUNCTION f(x):
    RETURN x²

// Define actual derivative f'(x) = 2x for comparison
FUNCTION actual_derivative(x):
    RETURN 2x

// Calculate derivative using forward difference method
FUNCTION calculate_numerical_derivative(f, x, step):
    RETURN (f(x + step) - f(x)) / step

// MAIN PROGRAM
BEGIN
    // Initialize parameters
    SET point = 2.0
    SET step_sizes = [0.1, 0.01, 0.001]

    // Calculate exact derivative
    SET exact_result = actual_derivative(point)
    DISPLAY "True derivative value: " + exact_result

    // Calculate approximate derivatives for each step size
    FOR each step IN step_sizes:
        SET approximate_result = calculate_numerical_derivative(f, point, step)
        DISPLAY "Using step=" + step + ": Result=" + approximate_result

    // Create visualization
    SET x_range = generate_points(0 to 4, count=100)
    
    // Plot main function
    PLOT x_range vs f(x_range) AS "x² function"
    MARK POINT (point, f(point)) IN RED
    
    // Add tangent lines
    FOR each step IN step_sizes:
        SET tangent = exact_result × (x_range - point) + f(point)
        PLOT tangent AS DASHED LINE
    
    // Add graph details
    SET TITLE "Numerical Differentiation Experiment"
    SET X_LABEL "x"
    SET Y_LABEL "f(x)"
    ADD LEGEND
    DISPLAY PLOT
END
