# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# ---------------- SAMPLE DATA ----------------

x = [1, 2, 3, 4, 5]
y = [2, 8, 18, 32, 50]


# ---------------- PLOT ORIGINAL DATA ----------------

plt.scatter(x, y, label="Original Data")


# ---------------- LINEAR INTERPOLATION ----------------

# Create interpolation function
linear_interp = interp1d(x, y, kind="linear")

# Generate 100 points between min(x) and max(x)
x_interp_linear = np.linspace(min(x), max(x), 100)

# Get interpolated y-values
y_interp_linear = linear_interp(x_interp_linear)

# Plot linear interpolation
plt.plot(
    x_interp_linear,
    y_interp_linear,
    label="Linear Interpolation"
)


# ---------------- CUBIC SPLINE INTERPOLATION ----------------

# Create cubic interpolation function
cubic_interp = interp1d(x, y, kind="cubic")

# Get cubic interpolated y-values
y_interp_cubic = cubic_interp(x_interp_linear)

# Plot cubic spline interpolation
plt.plot(
    x_interp_linear,
    y_interp_cubic,
    label="Cubic Spline Interpolation"
)


# ---------------- GRAPH SETTINGS ----------------

plt.title("Interpolation Exercise")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()

plt.grid(True)

# Display plot
plt.show()
