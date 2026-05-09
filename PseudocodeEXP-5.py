# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Generate sample data
x = [1, 2, 3, 4, 5]
y = [2, 8, 18, 32, 50]

# Plot original data
scatter(x, y, label="Original Data")

# Linear interpolation
linear_interp = interp1d(x, y, kind="linear")
x_interp_linear = generate 100 points between min(x) and max(x)
y_interp_linear = linear_interp(x_interp_linear)
plot(x_interp_linear, y_interp_linear, label="Linear Interpolation")

# Cubic spline interpolation
cubic_interp = interp1d(x, y, kind="cubic")
y_interp_cubic = cubic_interp(x_interp_linear)
plot(x_interp_linear, y_interp_cubic, label="Cubic Spline Interpolation")

# Show the plot
set title "Interpolation Exercise"
set xlabel "X-axis"
set ylabel "Y-axis"
add legend
display plot
