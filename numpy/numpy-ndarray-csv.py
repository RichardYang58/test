import numpy as np

# a=np.arange(100).reshape(5,20)
# np.savetxt('a.csv',a,fmt='%1f',delimiter=',')

# b=np.loadtxt('a.csv',delimiter=',')
# print(b)



#多維讀取檔案
a=np.arange(100).reshape(5,10,2)
# a.tofile("b.dat",sep=",",format='%d')
# c=np.fromfile("b.dat",dtype=np.int,sep=',').reshape(5,10,2)
# print(c)
np.save("a.npy",a)
b=np.load("a.npy")
print(b)