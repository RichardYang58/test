import pandas as pd
<<<<<<< HEAD
# data=pd.Series([30,15,20])
# # condition=[True,False,True]
# condition=data>18
# print(condition)
# filteredData=data[condition]
# print(filteredData)

# data=pd.Series(["你好","Python","Pandas"])
# condition=data.str.contains("P")
# # condition=[False,True,True]
# filteredData=data[condition]
# print(filteredData)

=======
>>>>>>> d19b82f32e5f52d9b9063a0812466d85dcda154b
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,40000,40000]
}, index=["a","b","c"])
<<<<<<< HEAD




=======
# print(data)
condition=data["salary"]>=40000
filteredData=data[condition]
print(filteredData)
>>>>>>> d19b82f32e5f52d9b9063a0812466d85dcda154b
