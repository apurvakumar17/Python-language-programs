import numpy as np
list1 = [1,2,3,4,5]
list2 = [[1,2,3], [4,5,6], [7,8,9]]
nd1 = np.array(list1)
nd2 = np.array(list2)
print(nd1)
print(nd2)
nd3=np.zeros(4)
print(nd3)
nd4=np.zeros(9).reshape(3,3)
print(nd4)
nd5=np.ones((4,5))
print(nd5)
print(np.mean(nd2))
print(np.sum(nd2,axis=1))