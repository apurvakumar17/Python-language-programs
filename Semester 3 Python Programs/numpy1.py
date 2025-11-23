import numpy as np
import random
arr = [0, 1, 2, 3]
print(np.array(arr))
print(np.zeros(10))
print(np.ones(12))
print(np.arange(0, 12, 2))
print(np.linspace(0, 10, 5))

print(random.randint(1,10))
print(random.random())

print(np.random.random())
print(np.random.rand(5))
print(np.random.randint(1,10,size = 10))

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1 + arr2)

print(type(np.sum(arr1)))
print(type(arr1))

arr33 = [[1,2,3], [4,5,6], [7,8,9]]
print(arr33, end="\n\n")
ndarr33 = np.array(arr33)
print(ndarr33, end="\n\n")
print(ndarr33.T)