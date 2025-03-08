import matplotlib.pyplot as plt
import numpy as np
#from matplotlib import colormaps

def potential_charge(X, Y, q, position):
    X1 = X - position[0]
    Y1 =  Y- position[1]
    R = (np.sqrt(X1**2 + Y1**2))
    if (R.all() == 0):
        R = 1e-9
    return q/(4*np.pi*e0)*(1/R)
def potential_field(X, Y):
    V1 = potential_charge(X, Y, -q, (1, 0))
    V2 = potential_charge(X, Y, q, (0, -1))
    V3 = potential_charge(X, Y, -q, (-1, 0))
    V4 = potential_charge(X, Y, q, (0, 1))
    #V = V1 + V2 + V3 + V4
    return V1+V2+V3+V4
q = 1
e0 = 8.854e-12

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)

#V = np.zeros_like(Y)

V = potential_field(X, Y)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, V, cmap="plasma", edgecolor="none")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Potential")
plt.savefig("../figs/pot.png")
plt.show()


