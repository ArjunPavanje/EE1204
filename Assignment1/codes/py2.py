import matplotlib.pyplot as plt
import numpy as np

phi = np.pi/4
s = np.linspace(-10, 10, 200)
F = np.sqrt((160/((s**2+1)**2)) + 22 + (240*np.sqrt(2)/(s**2 + 1))  )

plt.plot(s, F, label="|F| vs s")
plt.legend()
plt.xlabel("s")
plt.ylabel("|F|")
plt.title("|F| at $\phi=\pi/4$")
plt.savefig("../figs/fig2.png")
plt.show()
