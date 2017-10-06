from scipy import io as sp
from scipy import misc
import numpy as np
from random import randint
import os
sources_path = 'sources/'
a = np.ones((3, 3))
if os.path.exists(sources_path+'file.mat'):
    print 'file have existed'
else:
    sp.savemat(sources_path+'file.mat', {'a': a})
data = sp.loadmat(sources_path+'file.mat')
print data['a']
m = [[[0.5, 0.5, 0.2], [1, 0.5, 0.2], [1, 0.5, 0.2]],
     [[1, 1, 1], [1, 0.5, 0.2], [1, 0.5, 0.2]],
     [[1, 0.5, 0.2], [0, 0, 0], [1, 0.5, 0.2]]]
n = [[[randint(0, 255) for z in range(3)]for x in range(100)] for y in range(10)]
b = np.array(n)
if os.path.exists(sources_path+'zhs.png'):
    print 'image have existed'
else:
    misc.imsave(sources_path+'zhs.png', b)
x = misc.imread(sources_path+'lena.jpg')
misc.imsave(sources_path+'zhs1.png', x)



