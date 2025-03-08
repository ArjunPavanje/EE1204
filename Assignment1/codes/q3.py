import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the hemisphere parameters
a = 1  # Radius of the hemisphere

# Generate theta and phi values for the hemisphere surface
theta = np.linspace(0, np.pi / 2, 100)  # Theta ranges from 0 to pi/2 (hemisphere)
phi = np.linspace(0, 2 * np.pi, 100)    # Phi ranges from 0 to 2*pi (full circle)
theta, phi = np.meshgrid(theta, phi)

# Convert spherical coordinates to Cartesian coordinates
x = a * np.sin(theta) * np.cos(phi)
y = a * np.sin(theta) * np.sin(phi)
z = a * np.cos(theta)

# Plot the hemisphere surface
ax.plot_surface(x, y, z, color='b', alpha=0.5)

# Add field lines pointing upwards (in z-direction)
field_points = [
    (0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5),
    (0.7, -0.3, 0.6),
    (-0.7, 0.3, 0.6),
    (0, 0, 1)
]

for point in field_points:
    x_start, y_start, z_start = point
    ax.quiver(
        x_start, y_start, z_start,   # Starting point of the arrow
        0, 0, 1,                    # Direction vector (upward in z-direction)
        color='r', length=0.4       # Arrow properties
    )

# Set axis labels and limits for better visualization
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
ax.set_zlim([0, 1.2])

#plt.show()
plt.savefig("../figs/q3.png")
