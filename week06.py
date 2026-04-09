import numpy as np

l1 = [1, 2, 3]
array01 = np.array(l1)
print(l1)
print(array01)

array02 = np.arange(0, 10, 2)
print(array02)

array03 = np.zeros((2, 3))
print(array03)

array04 = np.ones((2, 3))
print(array04)

array05 = np.full((2, 3), 5)
print(array05)

array06 = np.random.rand(2, 3)
print(array06)

# array07 = np.random.random((2, 3, 3))
array07 = np.random.random((4, 2))
print(array07)
print(array07.shape, array07.dtype, array07.ndim, array07.size)
print(array07.T)

array08 = np.linspace(0, 10, 5)
print(array08)