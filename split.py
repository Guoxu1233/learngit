import numpy as np
#np.random.seed(10)
a = np.random.randint(20, size=10)
print(a)
b = np.argsort(a)
print(b)
print(a[b])