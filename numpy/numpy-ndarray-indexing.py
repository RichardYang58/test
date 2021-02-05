import numpy as np
# data=np.array([1,5,2,10])
# print(data[2])

# data=np.array([
#     [0,1],
#     [10,-5],
#     [2,6]
# ])
# print(data[0,1])

# data=np.array([1,5,2,10])
# print(data[0:3])
# print(data[:2])

# data=np.array([
#     [0,1,3], [10,-5,1],
#     [2,6,5], [2,1,0]
# ])
# print(data[1:3,0:2])

# data=np.array([
#     [
#         [0,1,3],
#         [10,-5,1]
#     ],    
#     [
#         [2,6,5],
#         [2,1,0]
#     ]
# ])
# print(data[0,...])

# a=np.linspace(1,10,4,endpoint=False)
# print(a)
# a=np.linspace(1,10,4)
# b=np.linspace(1,10,4,endpoint=False)
# c=np.concatenate((a,b))
# print(c)


a=np.arange(24).reshape((2,3,4))
# print(a)
# print(a[1,2,3])
# print(a[:,1,-3])
# print(a[:,1:3,:])
print(a[:,:,::2])

