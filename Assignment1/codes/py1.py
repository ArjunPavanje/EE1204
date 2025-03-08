import matplotlib.pyplot as plt
import numpy as np

phi = np.linspace(-10, 10, 200)
F = np.sqrt(38 + 24*(np.cos(phi) + np.sin(phi)))

plt.plot(phi, F, label="|F|" )
plt.legend()
plt.xlabel("s")
plt.ylabel("|F|")
plt.title("|F| at $s=3$ ")
plt.savefig("../figs/fig1.png")
plt.show()
