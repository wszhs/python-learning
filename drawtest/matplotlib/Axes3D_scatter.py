
import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
sources_path = 'sources/'
mat1 = sources_path+'4a.mat'
data = sio.loadmat(mat1)
m = data['data']

x, y, z = m[0], m[1], m[2]
ax = plt.subplot(111, projection='3d')

ax.scatter(x[:1000], y[:1000], z[:1000], c='y')
ax.scatter(x[1000:4000], y[1000:4000], z[1000:4000], c='r')
ax.scatter(x[4000:], y[4000:], z[4000:], c='g')

ax.set_zlabel('Z') 
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
