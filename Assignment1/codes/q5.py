import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plate dimensions
plate_length = 4
plate_width = 4
plate_separation = 2  # Distance between plates (z-axis)

# Draw the plates
# Bottom plate (z=0)
x_bottom = np.linspace(-plate_length / 2, plate_length / 2, 10)
y_bottom = np.linspace(-plate_width / 2, plate_width / 2, 10)
x_bottom, y_bottom = np.meshgrid(x_bottom, y_bottom)
z_bottom = np.zeros_like(x_bottom)  # z=0 for bottom plate
ax.plot_surface(x_bottom, y_bottom, z_bottom, color='gray', alpha=0.8)

# Top plate (z=d)
z_top = np.ones_like(x_bottom) * plate_separation  # z=d for top plate
ax.plot_surface(x_bottom, y_bottom, z_top, color='gray', alpha=0.8)

# Add labels to plates
ax.text(0, -plate_width / 2 - 1, 0, "Grounded (0 V)", color="black", fontsize=12)
ax.text(0, -plate_width / 2 - 1, plate_separation, "Raised Potential (V₀)", color="black", fontsize=12)

# Electric field lines
num_lines = 8
x_field = np.linspace(-plate_length / 4, plate_length / 4, num_lines)
y_field = np.linspace(-plate_width / 4, plate_width / 4, num_lines)
for x in x_field:
    for y in y_field:
        ax.plot([x, x], [y, y], [0, plate_separation], color='blue', linewidth=1.5)

# Add material label in the middle
ax.text(0, 0, plate_separation / 2, "Material with\nρ₀ and ε", color="black", fontsize=14,
        horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='white', edgecolor='black'))

# Set axis limits and labels
ax.set_xlim([-plate_length / 2 - 1, plate_length / 2 + 1])
ax.set_ylim([-plate_width / 2 - 1, plate_width / 2 + 1])
ax.set_zlim([0, plate_separation + 1])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Set title
ax.set_title("3D Parallel-Plate Capacitor with Electric Field Lines", fontsize=16)

# Show the plot
#plt.show()

plt.savefig("../figs/q5.png")

