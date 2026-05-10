# ---------------- IMPORT LIBRARIES ----------------

import numpy as np


# ---------------- OBJECTIVE FUNCTION ----------------

# Function to minimize:
# f(x) = sum of squared components
def objective(vector):

    return np.sum(vector**2)


# ---------------- PARTICLE SWARM OPTIMIZATION ----------------

def particle_swarm_optimization(
    objective_function,
    min_bounds,
    max_bounds,
    num_particles=30,
    max_iterations=100,
    inertia=0.5,
    cognitive=1.5,
    social=1.5
):

    dimensions = len(min_bounds)

    # ---------------- INITIALIZE PARTICLES ----------------

    positions = np.random.uniform(
        min_bounds,
        max_bounds,
        (num_particles, dimensions)
    )

    velocities = np.random.uniform(
        -1,
        1,
        (num_particles, dimensions)
    )

    # Personal best positions
    personal_best_positions = np.copy(positions)

    # Personal best values
    personal_best_values = np.array([
        objective_function(p)
        for p in positions
    ])

    # Global best
    global_best_index = np.argmin(personal_best_values)

    global_best_position = personal_best_positions[
        global_best_index
    ]

    global_best_value = personal_best_values[
        global_best_index
    ]


    # ---------------- MAIN LOOP ----------------

    for iteration in range(max_iterations):

        for i in range(num_particles):

            # Random coefficients
            r1 = np.random.rand(dimensions)

            r2 = np.random.rand(dimensions)

            # Update velocity
            velocities[i] = (
                inertia * velocities[i]
                + cognitive * r1 * (
                    personal_best_positions[i]
                    - positions[i]
                )
                + social * r2 * (
                    global_best_position
                    - positions[i]
                )
            )

            # Update position
            positions[i] = positions[i] + velocities[i]

            # Keep inside bounds
            positions[i] = np.clip(
                positions[i],
                min_bounds,
                max_bounds
            )

            # Evaluate objective
            current_value = objective_function(
                positions[i]
            )

            # Update personal best
            if current_value < personal_best_values[i]:

                personal_best_positions[i] = positions[i]

                personal_best_values[i] = current_value

            # Update global best
            if current_value < global_best_value:

                global_best_position = positions[i]

                global_best_value = current_value


    return global_best_position, global_best_value


# ---------------- MAIN PROGRAM ----------------

# Search bounds
min_bounds = np.array([-5, -5, -5])

max_bounds = np.array([5, 5, 5])


# Run PSO
best_position, best_value = particle_swarm_optimization(
    objective_function=objective,
    min_bounds=min_bounds,
    max_bounds=max_bounds
)


# ---------------- RESULTS ----------------

print("Best position found:")

print(best_position)

print("\nBest value found:")

print(best_value)
