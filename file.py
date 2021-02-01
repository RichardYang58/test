# file=open("data.txt",mode="w",encoding="utf-8")
# file.write("中文\nSecond line")
# file.close()

with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n3")
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file:
    # data=file.read()
    for line in  file:
        sum+=int(line)
      
print(sum)

import json
with open("config.json", mode="r") as file:
    data=json.load(file)    
# print("name",data["name"])
# print("version",data["version"])
data["name"]="New Name"
with open("config.json", mode="w") as file:
    json.dump(data,file)





