# import numpy as np
# import matplotlib.pyplot as plt
# import math
# q = np.linspace(0, 2*math.pi, num=100)
# x = np.sin(q)
# y = np.cos(q)
# plt.figure(figsize=(8, 8))
# plt.plot(x, y, label="draw", color="red", linewidth=2)
# plt.xlabel("x value")
# plt.ylabel("y value")
# plt.title("function")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
q = np.linspace(0, 2*np.pi, num=10)
q2 = np.linspace(0, 2*np.pi, num=20)
# y = np.cos(q)+np.sin(q)*1.0j
# y2 = np.e**(q2*1.0j)
y = q + 1.0j
y2 = q2
plt.figure(figsize=(8, 8))
plt.plot(q, y, label="draw", color="red", linewidth=2)
plt.plot(q2, y2, label="draw", color="yellow", linewidth=1)
plt.xlabel("x value")
plt.ylabel("y value")
plt.title("function")
plt.show()
