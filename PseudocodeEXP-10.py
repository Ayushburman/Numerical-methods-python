// Define function to minimize: sum of squared components
FUNCTION objective(vector):
    RETURN sum(each component squared)

// MAIN PSO ALGORITHM
BEGIN
    // Define search space
    SET min_bounds = [-5, -5, -5]
    SET max_bounds = [5, 5, 5]

    // PSO Algorithm
    FUNCTION particle_swarm_optimization:
        // Initialize particles
        CREATE particle swarm with random positions
        SET each particle's best position to current
        SET global best to best among all particles

        // Main loop
        WHILE not converged AND iterations < max_iterations:
            FOR each particle:
                UPDATE velocity
                UPDATE position within bounds
                EVALUATE objective_function
                UPDATE particle's best if improved
                UPDATE global best if improved

        RETURN global_best_position, global_best_value

    // Run optimization
    SET best_position, best_value = particle_swarm_optimization(
        function: objective
        min_bounds: min_bounds
        max_bounds: max_bounds
    )

    // Show results
    DISPLAY "Best position found: " + best_position
    DISPLAY "Best value found: " + best_value
END
