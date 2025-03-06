import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps

def E_charge(X, Y, q, position):
    X1 = X - position[0]
    Y1 =  Y- position[1]
    norm = np.sqrt(X1**2 + Y1**2)
    return q/(4*np.pi*e0)*(X-position[0])/norm**3, q/(4*np.pi*e0)*(Y-position[1])/norm**3 

def E_field(X, Y):
    E1 = E_charge(X, Y, q, (1, 0))
    E2 = E_charge(X, Y, q, (0, 1))
    E3 = E_charge(X, Y, q, (-1, 0))
    E4 = E_charge(X, Y, q, (0, -1))
    return E1[0]+E2[0]+E3[0]+E4[0], E1[1]+E2[1]+E3[1]+E4[1] 

q = 1
e0 = 8.854e-12

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

U, V = E_field(X, Y)

# Compute the magnitude of the vectors
magnitude = np.sqrt(U**2 + V**2)

for i in range(0, len(magnitude)):
    for j in range(0, len(magnitude)):
        if magnitude[i][j] > 1e11:
            magnitude[i][j] = 0

# Plot using quiver, setting the color using a colormap
plt.figure(figsize=(6, 6))
quiver_plot = plt.quiver(X, Y, U/magnitude, V/magnitude, magnitude, cmap='plasma')

# Add a colorbar
plt.colorbar(quiver_plot, label='Magnitude')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Vector Field")
plt.show()
plt.show()
