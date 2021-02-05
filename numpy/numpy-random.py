import numpy as np
# sn=np.random.randn(3,4,5)
# print(sn)

# b=np.random.randint(100,200,(3,4))
# print(b)

# np.random.seed(10)
# b=np.random.randint(100,200,(3,4))
# print(b)

# a=np.random.randint(100,200,(3,4))
# print(a)
# np.random.shuffle(a)
# print(a)
# np.random.shuffle(a)
# print(a)

# b=np.random.randint(100,200,(8,))
# print(b)
# c=np.random.choice(b,(3,2),replace=False)
# print(c)

# b=np.random.randint(100,200,(8,))
# c=np.random.choice(b,(3,2),p=b/np.sum(b))
# print(c)

# u=np.random.uniform(0,10,(3,4))
# print(u)
# u=np.random.normal(10,5,(3,4))
# print(u)

#統計函數
# a=np.arange(15).reshape(3,5)
# print(a)
# print("sum ", np.sum(a))
# print("mean axis=1", np.mean(a,axis=1))
# print("mean axis=0", np.mean(a,axis=0))
# print("average",np.average(a,axis=0,weights=[10,5,1]))
# print("std",np.std(a))
# print("var",np.var(a))


# a=np.arange(15,0,-1).reshape(3,5)
# print(a)
# print("max",np.max(a))
# print("argmax",np.argmax(a))
# print("unravel",np.unravel_index(np.argmax(a),a.shape))
# # print("ptb",np.ptb(a))
# print("median",np.median(a))

# a=np.random.randint(0,20,(5))
# print(a)
# print(np.gradient(a))
a=np.random.randint(0,20,(3,5))
print(a)
print(np.gradient(a))

