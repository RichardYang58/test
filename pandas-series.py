import pandas as pd
# data=pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"])
# print(data)

# print("資料型態",data.dtype)
# print("資料數量",data.size)
# print("資料索引",data.index)

# print(data[2],data[0])
# print(data["e"],data["d"])

# print("最大值",data.max())
# print("總和",data.sum())
# print("標準差",data.std())
# print("中位數",data.median())
# print("最大三個",data.nlargest(3))
# print("最小三個",data.nsmallest(3))

data=pd.Series(["你好","Python","Pandas"])
# print(data.str.lower())
# print(data.str.len())
print(data.str.cat(sep=","))
print(data.str.contains("P"))


