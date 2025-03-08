import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the cylinder
radius = 1
height = 5

# Create the cylinder
z = np.linspace(0, height, 100)
theta = np.linspace(0, 2 * np.pi, 100)
Z, Theta = np.meshgrid(z, theta)
X = radius * np.cos(Theta)
Y = radius * np.sin(Theta)

# Plot the cylinder
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, rstride=5, cstride=5, edgecolor='k', linewidth=0.5)

# Mark points: center point, surface point, and outside point
center_point = [0, 0, height / 2]
surface_point = [radius, 0, height / 2]
outside_point = [2 * radius, 2 * radius, height / 2]

ax.scatter(*center_point, color='red', label='Center Point')  # Center point
ax.scatter(*surface_point, color='blue', label='Surface Point')  # Surface point
ax.scatter(*outside_point, color='green', label='Outside Point')  # Outside point

# Draw an arrow from the outside point to the z-axis (center of cylinder)
arrow_start = outside_point
arrow_end = [0, 0, height / 2]  # Projected to z-axis
ax.quiver(
    arrow_start[0], arrow_start[1], arrow_start[2],
    arrow_end[0] - arrow_start[0], arrow_end[1] - arrow_start[1], arrow_end[2] - arrow_start[2],
    color='purple', linewidth=1.5, label='Arrow to Z-axis'
)

# Labels and legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

plt.show()
#plt.savefig("../figs/q4.png")
