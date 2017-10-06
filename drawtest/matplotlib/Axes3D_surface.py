import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math

fig = plt.figure()
ax = Axes3D(fig)

p = np.linspace(0, 2*math.pi, num=10)
q = np.linspace(0, 2*math.pi, num=10)
x = np.cos(p)*np.cos(q)
y = np.sin(p)*np.cos(q)
x, y = np.meshgrid(x, y)
z = np.sin(q)

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')

plt.show()