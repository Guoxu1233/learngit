import numpy as np
a = np.arange(9).reshape(3,3)
print(a)
b = np.transpose(a)
temp = np.copy(b[0])
b[0] = b[1]
b[1] = temp
c = np.transpose(b)
print(c)