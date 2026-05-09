DEFINE function f(x):
    RETURN x²

DEFINE function actual_derivative(x):
    RETURN 2x

DEFINE function calculate_derivative(f, x, step_size):
    RETURN (f(x + step_size) - f(x)) / step_size

// Main program
SET test_point = 2.0
SET step_sizes = [0.1, 0.01, 0.001]

// Calculate and print true derivative at test point
SET true_result = actual_derivative(test_point)
PRINT true_result

// Test different step sizes
FOR EACH step IN step_sizes:
    SET approximated_derivative = calculate_derivative(f, test_point, step)
    PRINT approximated_derivative

// Visualization
PLOT:
    - Draw function x² from x=0 to x=4
    - Mark point (2, f(2)) with a dot
    - Draw tangent lines at x=2 for each step size
    - Add labels and legend
    - Display graph
