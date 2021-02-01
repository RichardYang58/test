import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")
# print(data)

import json
src="https://data.taipei/api/getDatasetInfo/downloadResource?id=15c3e1ae-899b-466c-a536-208497e3a369&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as response:
    data=json.load(response)
print(data)
clist=data["result"]["results"]
print(clist)
with open("data.txt","w",encoding="utf-8") as file: 
     for company in clist:
         file.write(company["公司名稱"]+"\n")
