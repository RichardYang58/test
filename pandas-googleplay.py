import pandas as pd
data=pd.read_csv("googleplaystore.csv")
# print(data.shape)
# print(data.columns)
# print("=======================")
# condition=data["Rating"]<=5
# data=data[condition]
# print(data["Rating"].mean())
# # print(data["Rating"].nlargest(100).mean())

# print(data["Installs"].mean())
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
condition=data["Installs"]>100000
print("你好",data[condition].shape[0])

keyword=input("請輸入")
condition=data["App"].str.contains(keyword,case=False)
print(data[condition]["App"])




