import numpy as np
# data=np.ones(10)
# print(data)
# data=np.array([
#     [3,1,5],
#     [1,2,3]
# ])
# print(data.shape)

# data=np.array([
#     [3,1,5],
#     [1,2,3]
# ])
# print(data.shape)
# print(data.T.shape)
# data=np.array([
#     [
#         [3,1,5],[1,2,3]
#     ],
#     [
#         [0,2,1],[3,4,1]
#     ]    
# ])
# newData=data.ravel()
# print(newData)
# print(newData.shape)

# data=np.array([
#     [
#         [3,1,5],[1,2,3]
#     ],
#     [
#         [0,2,1],[3,4,1]
#     ]    
# ])
# newData=data.reshape(3,4)
# print(newData)

# data=np.arange(9).reshape(3,3)
# print(data)

a=np.ones((2,3,4),dtype=np.int32)
# print(a)
# b=a.reshape((3,8))
# print(b)
# a.resize((3,8))
# print(a)

# b=a.flatten()
# print(b)

# b=a.astype(np.float)
# print(b)

a=np.full((2,3,4),25,dtype=np.int32)
print(a)
b=a.tolist()
print(b)