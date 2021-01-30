import pandas as pd
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,40000,40000]
}, index=["a","b","c"])
# print(data)
condition=data["salary"]>=40000
filteredData=data[condition]
print(filteredData)
