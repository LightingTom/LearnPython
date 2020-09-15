import numpy as np

zero = np.zeros((10,10))
zero[0] = 1
zero[9] = 1
zero[:,0] = 1
zero[:,9] = 1

b = np.arange(0,5)
res = np.hstack((b,b,b,b,b))
res = res.reshape(5,5)
# print(res)

c = np.array([[0,1],[1,0]])
res_3 = np.tile(c,(4,4))
# print(res_3)

d = np.array([0,1,2,3,4,5,6,7,8,9])
res_4 = d[(d%2==1)]
# print(res_4)

print(5 or 3)