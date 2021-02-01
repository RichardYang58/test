import pandas as pd
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,40000,40000]
}, index=["a","b","c"])
print(data)
print("==================================")
# print("資料數量",data.size)
# print("資料型態",data.shape)
# print("資料索引",data.index)

# print("取的第二列",data.iloc[1], sep="\n")
# print("==================================")
# print("取的第c列",data.loc["c"], sep="\n")

# print("取的name欄",data["name"],sep="\n")
# names=data["name"]
# print("把name轉大寫",names.str.upper(),sep="\n")
# salaries=data["salary"]
# print("取平均值",salaries.mean())

data["revenue"]=[500000,400000,300000]
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])
data["cp"]=data["revenue"]/data["salary"]
print(data)

