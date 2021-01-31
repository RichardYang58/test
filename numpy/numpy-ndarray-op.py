import numpy as np
# data1=np.array([3,2,10])
# data2=np.array([1,3,6])
# result=data1+data2
# print("加法",result)
# result=data1*data2
# print("乘法",result)
# result=data1>data2
# print("大於",result)

# data1=np.array([
#     [1,3]
# ])

# data2=np.array([
#     [2,-1,3],
#     [-2,4,1]
# ])
# result=data1.dot(data2)
# print(result)
# result=data1@data2
# print(result)
# result=np.outer(data1,data2)
# print(result)

data=np.array([
    [2,1,7],
    [-5,3,8]
])
# result=data.sum()
# print("總和",result)
# result=data.mean()
# print("平均數",result)
# result=data.max()
# print("最大",result)

# result=data.sum(axis=0)
# print(result)
# result=data.sum(axis=1)
# print(result)
# result=data.max(axis=0)
# print(result)
result=data.cumsum(axis=0)
print(result)

